#-*-coding:utf-8-*-  
#author:Lizr
#date:2013-1-25
#游戏错误提示语言包

lang = {
#网络通讯错误
-11111111:'协议号未定义,或程序未更新!',
-22222222:'程序运行错误!',
-33333333:'协议号未定义 或返回出错',
-88888888:'未登录',


#尾数为999的错误编号会自动取这语言包
999:'参数错误', 
998:'非法操作',
997:'系统错误 ',
996:'操作失败 ',
995:'支付失败 ',
994:'货币不足',
993:'长度不符合要求', #输入XX名称时
992:'不能含有敏感字符',
991:'存在特殊字符',
990:'',

901:'建筑不存在或不属于你',
902:'建筑正在建造',
903:'该建筑不是招贤馆',
904:'建筑工匠数量不足',
905:'建筑正在升级',

910:'装备不存在',#装备系统

920:'军团不存在',#外史院——军团科技

930:'1',

940:'1',

950:'1',

960:'1',

970:'1',

980:'1',
#尾数900以上是公共语言包
-10001001:'先注册',
-10001002:'登陆失败',
-10001003:'登录验证失败',

-10002001:'创建失败，用户昵称已存在',
-10002002:'创建失败',
-10002003:'登录失败',
-10002004:'阵营不正确',
-10002005:'头像不正确',


-13001001:'已达最大工匠',

-11001001:'聊天间隔限制',
-11001002:'消息未通过验证',
-11001003:'发送对象不在线',
-11001004:'喇叭不足，请购买后再发送消息',
-11001005:'不能私聊自己',
-11001006:'权限不足',
-11001007:'您已经被禁言，请文明发言',

#背包
-13062001:'背包位置不合法',
-13062002:'当前位置没有物品',
-13063001:'背包空间已达最大',

-14002002:'所传的坐标非可购买坐标的起点',
-14002003:'你已经购买过此坐标',
-14002004:'购买失败',


#武馆
-15090001:"玩家没有该建筑",
-15090002:"武馆正在建造",
-15090003:"建筑不是武馆",
-15090004:"玩家没有该武将",
-15090005:"武将正在训练",
-15090006:"训练位已满",
-15090007:"训练时间不正确",
-15090008:"支付失败",

-15091001:"该武将没训练",
-15091002:"支付失败",
-15091003:"增加货币失败",
-15091004:"Flag不正确",

-15093001:"玩家没有该建筑",
-15093002:"武馆正在建造",
-15093003:"建筑不是武馆",
-15093004:"玩家没有该武将",
-15093005:"需要等待冷却时间结束",
-15093006:"已达到当天的最大突飞训练次数",
-15093007:"扣钱失败",

-15094001:"冷却时间为0",
-15094002:"扣钱失败",

#点将台
-15010998:"没有该点将台",
-15010997:"用户没有该武将",
-15010001:"该武将所有培养属性已达等级上限，不可培养",
-15010002:"货币类型错误",
-15010003:"金钱不够",
-15010004:"培养次数不足",
-15010005:"该武将无法进行将卡培养",
-15010006:"没有对应的武将卡",

-15011001:"没有该武将的培养信息",
-15011002:"没有该武将",

-15012001:"用户没有该武将",

-15013001:"获取武将信息失败",

-15014998:"用户没有点将台",

-15015001:"玩家无此武将",
-15015002:"装备部位出错",
-15015003:"没有换装",
-15015004:"装备不存在",
-15015005:"装备正被其他武将穿着",
-15015006:"没达到可穿戴等级",
-15015007:"强化等级高于武将等级",
-15015008:"该装备不能穿在该部位",

-15016001:"玩家无此武将",
-15016002:"装备部位不正确或该武将在该部位上没有装备，无法脱下",





-15001001:'坐标已被占用',
-15001002:'未达到开放等级',
-15001003:'无空闲工匠',
-15001004:'已达到最大建筑数量',
-15001005:'目前等级未可建这么多家',

-15002001:'用户没有该建筑',
-15002002:'不是空闲状态的建筑，无法升级',
-15002003:'建筑已达最高等级',
-15002004:'已达最高等级，请升级将军府',

-15003004:'建筑已建造或升级完成，不能取消。',

-15004002:'没有这个建筑',
-15004003:'用户没有该建筑',
-15004004:'建筑已建造或升级完成',

#铸币厂，磨坊
-15005001:'没有可收集资源',
-15005002:'建筑修复中',


#招贤馆
-15006001:'招募表中无记录',

-15007001:'此武将不可招募',
-15007002:'已有该类型武将',
-15007003:'没有剩余的点将台',
-15007004:"该武将不存在", 

#效场
-15102001:'武将不在阵上无法移除',
-15102002:'阵上武将已满',
-15102003:'布阵操作失败',
-15103001:'该武将没上阵或没有该武将',
-15103002:'带兵数量过大',

#祭坛
-15020001:'数据库出错',
-15021001:'用户没有该建筑',
-15021002:'建筑不是祭坛',
-15021003:'建筑正在建造',
-15021004:'地坛的抽奖次数已到',
-15021005:'祭坛类型错误',
-15021006:'支付失败',
-15022001:'查询数据库出错',

#兵营
-15031001:'数量不能小于0 ',
-15031002:'不是士兵',
-15031003:'不是器械',
-15031004:'该玩家没有这个建筑',
-15031005:'建筑不在空闲状态',
-15031006:'该建筑不是兵营',
-15031007:'该建筑不是工坊',
-15031008:'没有达到开放等级',
-15031009:'超过了训练上限',
-15031010:'支付失败',
-15031011:'增加货币失败',
-15031012:'未改变数量',
-15032001:'雇佣数量必须大于0',
-15032002:'兵种不是雇佣兵',
-15032003:'玩家没有该建筑 ',
-15032004:'建筑正在建造',
-15032005:'建筑不是佣兵处',
-15032006:'大于校场屯兵数',
-15032007:'超过了雇佣上限',
-15032008:'支付失败',
-15032009:'用户当前没有征兵记录',
-15032010:'没有训练该兵种 ',
-15032011:'训练数量大于校场的剩余容量',
-15032012:'黄金不足',

#外史院 军团
-15060001:'你已加入军团，不能创建',
-15060002:'该军团名称已存在',
-15061001:'贡献越出今天最大限制',
-15064001:'只能加入一个军团',
-15064002:'军团成员已满',
-15064003:'该军团不允许加入',
-15076001:'科技已达最大等级',
-15082002:'贡献支付失败',
-15901003:'坐标已被占用',

#理藩院
-15121001:'不是玩家的藩国',
-15121002:'不可收集',
-15121003:'增加货币操作失败',
-15121004:'增加货币操作失败',
-15121005:'操作类型错误',

-15122001:'您并不是自由身，不能设置藩国',
-15122002:'要设置的玩家不是自由身',
-15122003:'不是手下败将',
-15122004:'玩家没有这个理藩院',
-15122005:'建筑正在建造   ',
-15122006:'建筑不是理藩院',
-15122007:'藩国数量已达最大',
-15122008:'设置藩国失败',
-15122009:'不能设自己的主人为藩国',
-15122010:'玩家处于调停中，无法设为潘国',

#铁匠铺
-16001002:'强化次数不足',
-16001003:'装备已达最大强化等级',
-16002001:'背包空间不足',
-16002002:'该装备不能购买',
-16002003:'购买该装备需要更高等级铁匠铺',

-16003001:'没有出售记录',
-16003002:'该物品不能回购',
-16003003:'背包空间不足',
-16004001:'物品不在背包中',
-16004002:'出售数量有误',
-16004003:'该道具不可出售',
-16004004:'没有足够空间存放铜钱',
-16004005:'装备不属于你',
-16004006:'出售失败',

#书院
-15052001:'学院正在学习中',
-15052002:'书院等级不足',
-15053001:'科技已完成学习',
#邮件
-18006001:'不能超过5个玩家',
-18006002:'不能发邮件给自己',
-18006003:'邮件信息不完整',
-18006004:'输入昵称有误',
-18005001:'背包已满',
-18005002:'该邮件没有附件',

#好友
-19003001:'好友超过上限',
-19003002:'对方好友已达上限',
-19006001:'半小时内不可重复删除好友',
-19010001:'用户不存在',
-19010002:'不能添加自己',
-19010003:'对方已经是好友',
-19010004:'当前好友已到达上限',
-19010005:'不可加不同阵营的玩家为好友',
-19010006:'好友删除30分钟内不能再次添加',
-19010007:'对方好友已达上限',

#道具
-20002001:'percent错误,大于1',
-20002002:'超过资源上限',
-20004001:'背包没有该道具',
-20004002:'使用等级不足',
-20004003:'道具不存在',
-20004004:'校场空间不足',
-20004005:'没有空闲点将台',
-20004006:'已拥有该类型武将',
-20004007:'没有铁匠铺',
-20004008:'强化次数已是最大值',
-20004009:'没有点将台',
-20004010:'培养次数已是最大值',
-20004011:'目前没有支配者',
-20004912:'用户不存在',
-20004013:'不是好友',
-20004014:'背包格子数已达上限',
-20004015:'该道具不可直接使用',
-20004016:'当前资源已达上限',
-20004017:'不同装备阵营的士兵',
-20004018:'背包空间不足',
-20005001:'装备不可出售',
-20006001:'商品不存在',
-20006002:'背包空间不足',
-20006003:'货币不足',

#拜访
-21001001:'用户不存在',
-21004001:'鲜花不足',
#活动系统
-23003001:'不能领取',
-23003002:'礼包已领取',
-23003003:'礼包已过期',
-23005001:'不能领取',
-23007001:'该日期已签',
-23007002:'不可在开服日期前补签',
-23007003:'没有重签次数',
-23007004:'货币不足',
-23008001:'抽奖次数已最大',
-23008002:'黄金不足',
-23011001:'可抽奖次数不足',

#比武
-24001001:'未达开放等级',
-24003001:'您今天已经领取过奖励',
-24003002:'不符合领取奖励条件',


#战役
-90001001:'尚未派兵出征,请先布阵',
-90001002:'越出每日可打上限',
-90001003:'战役未达到',
-91002001:'尚未派兵出征,请先布阵',
-91005001:'尚未派兵出征,请先布阵',
-91005002:'扫荡失败',

#城墙 布防
-92001001:'尺寸不合法',
-92001002:'坐标不合法',
-92001003:'超出最大可建筑数量',
-92006001:'超出可布防武将数量上限',

-92011001:'无可修复防御工事',
-92012001:'没有可回收的防御工事',


-93001001:'尚未派兵出征,请先布阵',
-93001002:'不可攻打自己',
-93001003:'无可匹配对象',
-93001004:'目标当前在线，不能攻打',
-93001005:'目标当前处于保护中，不能攻打',
-93001006:'目标当前正在被窥视或攻打中，请稍后再试',
-93001007:'获取匹配玩家失败，请稍后再试',
-93001008:'剩余行动力不足',
-93001009:'等级未达到，不可攻城',
-93001010:'战役未达到，不可攻打',

-93002001:'无效的匹配对象，不能开始攻城',
-93004001:'无效的匹配对象，不能同步战斗',
-93004002:'无效的战役，不能同步战斗',
-93009001:'无效的匹配对象，不能结束战斗',
-93009002:'无效的战役，不能结束战斗',

-94001001:'请先在校场布阵,派将兵上场',
-94001002:'越出每日可比武上限,请明日再战',
-94001003:'不可与自己比武',
#---------------------新的语言包加到下面,先不用按编号排 (上面已提交文案) --------------------------
#主角
-10005001:'该昵称已存在！',

-15112001:'成就不存在',
-15112002:'成就未达成',

#招贤馆新加协议
-15131001:"ItemId不正确或数量不足，兑换失败",

-15133001:"武将卡ID不正确",
-15133002:"武将卡数量不足",
-15133003:"背包空间不足",
-15133004:"武将卡数量不足(并发导致)",

#点将台
-15012002:"武将身上有装备，无法遣散",
-15016003:"向背包中增加装备失败",
-15010005:"货币类型错误",

#外史院
-15070001:"军团成员已满",
-15070002:"没有申请记录",
-15064004:'离上次退出军团时间间隔不符合要求',

# 装备
-16006001:"装备不存在",
-16006002:"源装备等级必须大于0",
-16006003:"目标装备等级已达最大",

-16007001:"升级物品不存在",
-16007002:"必须让武将穿戴才能升级",
-16007003:"已达最大等级",


}

if __name__ == '__main__':
    from sgLib.core import Gcore
    Gcore.printd(lang)