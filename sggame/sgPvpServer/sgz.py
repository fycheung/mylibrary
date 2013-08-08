#coding:utf8
#author:zhoujingjiang
#date:2013-04-16

import struct

import gevent
import gevent.server
import gevent.queue
import gevent.socket
import message

LEN_HEADER = '!I'
LEN_HEADER_SIZE = struct.calcsize(LEN_HEADER)

class Sender(object):
    def __init__(self, channel):
        self._queue = gevent.queue.Queue()
        self._channel = channel

    def put(self, buff):
        self._queue.put(buff)

    def loop(self):
        while True:
            buff = self._queue.get()
            packed_buff_len = struct.pack(LEN_HEADER, len(buff))
            try:
                result = self._channel._socket.sendall(packed_buff_len + buff)
            except Exception:
                break
            if result is not None:
                break

class Channel(object):
    _spawn = gevent.spawn

    def full(self):
        return False

    def set_spawn(self, spawn):
        if spawn == 'default':
            self.pool = None
            self._spawn = self._spawn
        elif hasattr(spawn, 'spawn'):
            self.pool = spawn
            self._spawn = spawn.spawn
        elif isinstance(spawn, (int, long)):
            from gevent.pool import Pool
            self.pool = Pool(spawn)
            self._spawn = self.pool.spawn
        else:
            self.pool = None
            self._spawn = spawn
        if hasattr(self.pool, 'full'):
            self.full = self.pool.full

    def __init__(self, sock, handle, spawn='default'):
        Channel.handle = staticmethod(handle)
        
        self.set_spawn(spawn)
        self._socket = sock
        self._socket.setsockopt(gevent.socket.SOL_TCP, gevent.socket.TCP_NODELAY, 1)
        self._socket.setsockopt(gevent.socket.IPPROTO_TCP, gevent.socket.TCP_NODELAY, 1)
        self.peername = self._socket.getpeername()
        self.sockname = self._socket.getsockname()

        self._closed = False
        self._sender = Sender(self)
        self._send_let = self._spawn(self._sender.loop)
        self._send_let.link(self.close)
        self._recv_let = self._spawn(self.loop)
        self._recv_let.link(self.close)

    def __str__(self):
        f, t = self.peername, self.sockname
        return '<%s.%s: from %s to %s>' % (
                self.__class__.__module__,
                self.__class__.__name__, f, t)

    def __repr__(self):
        return '<%s at %s>' % (str(self), hex(id(self)))

    def getsockname(self):
        return self._socket.getsockname()

    def getpeername(self):
        return self._socket.getpeername()

    def loop(self):
        def recv_bytes(bytes):
            buff = ''
            while len(buff) < bytes:
                t = self._socket.recv(bytes - len(buff))
                if not t:
                    return ''
                buff += t
            return buff

        def recv():
            try:
                buff = recv_bytes(LEN_HEADER_SIZE)
                if not buff:
                    return ''
                packet_len = int(struct.unpack(LEN_HEADER, buff)[0])

                if packet_len > 8 * 1024:
                    return ''

                buff = recv_bytes(packet_len)
                return buff
            except gevent.socket.error:
                return ''

        assert self._socket
        assert not self._closed
        while True:
            buff = recv()
            if not buff:
                break
            self._spawn(self._process_request, buff)
    
    def _process_request(self, buff):
        res = Channel.handle(self, buff)
        self._send(res)

    def _send(self, buff):
        if self._closed:
            return
        if buff is None:
            return
        if not isinstance(buff, basestring):
            self.close()
        else:
            self._sender.put(buff)

    def close(self, t = None):
        if self._closed:
            return
        self._closed = True
        self._spawn(self._real_close)

    def _real_close(self):
        if self._socket:
            self._socket.close()
            self._socket = None
        if self._send_let:
            self._send_let.kill()
            self._send_let = None
        if self._recv_let:
            self._recv_let.kill()
            self._recv_let = None
        self._sender = None

class Server(gevent.server.StreamServer):
    NEW_CONNECTION = 'Server.NEW_CONNECTION'
    LOST_CONNECTION = 'Server.LOST_CONNECTION'

    def __init__(self, listener, handle, backlog=None, spawn='default', **ssl_args):
        gevent.server.StreamServer.__init__(self,
                listener,
                self._handler,
                backlog,
                spawn,
                **ssl_args)
        Server._handle = staticmethod(handle)

    def __str__(self):
        return '<%s.%s:%s>' % (
                self.__class__.__module__,
                self.__class__.__name__,
                str(self.address))

    def __repr__(self):
        return '<%s at %s>' % (str(self), hex(id(self)))

    def _handler(self, sock, addr):
        channel = Channel(sock, Server._handle, self._spawn)
        message.pub(Server.NEW_CONNECTION, self, channel)
        channel._recv_let.join()
        message.pub(Server.LOST_CONNECTION, self, channel)

class Application(object):
    _spawn = gevent.spawn
    def __init__(self, *servers):
        self._servers = servers

    def run(self):
        jobs = [self._spawn(server.serve_forever) for server in self._servers 
                if hasattr(server, 'serve_forever')]
        gevent.joinall(jobs)