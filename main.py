import itchat , time
from itchat.content import *
import dataprocess
from apscheduler.schedulers.background import BackgroundScheduler

#为了每次唯一确定一个group
groupnametransfer = {}
#每3分钟进行一次存储
msgfromGroup=[]

#获取群成员聊天记录。
@itchat.msg_register(TEXT, isGroupChat=True)
def text_record(msg):
    global msgfromGroup
    # 格式为#群聊名#用户昵称#信息内容#时间   这里要注意群聊中的用户昵称会改变，同时要判断自己的昵称···\
    try:
        gname = groupnametransfer[msg['FromUserName']]
        if gname=='我':
            gname = groupnametransfer[msg['ToUserName']]
    except KeyError:
            gname='无关群聊'

    formatmsg='#'+gname+'#'+msg.actualNickName+'#'+msg.text+'#'+\
              time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'#'
    msgfromGroup.append(formatmsg)
    print(msgfromGroup[-1])
    #dataprocess.storetofile(msgfromGroup)

#通过群名称获取群成员列表
def getchatroom_friendlist(chatroomName):
    #chatroomName='拳头游戏2020校招交流群'
    #chatroomName = '软件学院1604'
    itchat.get_chatrooms(update=True)
    chatrooms = itchat.search_chatrooms(name=chatroomName)
    print(chatrooms)
    if chatrooms:#这里是有bug的··· 改成 if chatrooms 就好了，再改了一下逻辑。
        chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
        print(chatroom['UserName'])
        print(chatroom)
        for friend in chatroom['MemberList']:
            print('本群昵称：' + friend['DisplayName'] + '  #' '昵称:' + friend['NickName'])
            print(friend['DisplayName'] or friend['NickName'])
    else:
        print(u'没有找到群聊：' + chatroomName)


#作为定时运行函数，定时向群内发送任务
def send_msg(msgcontent, groupname):

    print('schedule execute')
    itchat.get_chatrooms(update=True)
    chatrooms = itchat.search_chatrooms(name=groupname)
    # chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
    itchat.send(msgcontent, chatrooms[0]['UserName'])

def getgname(namelist):
    global groupnametransfer
    for gname in namelist:
        itchat.get_chatrooms(update=True)
        chatrooms = itchat.search_chatrooms(name=gname)
        if chatrooms:
            chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
            groupnametransfer.setdefault(chatroom['UserName'], gname)

    #在这里将自己的username加进去s
    myusername=itchat.search_friends()
    groupnametransfer.setdefault(myusername['UserName'], '我')


def store():
    global msgfromGroup
    dataprocess.storetofile(msgfromGroup)
    msgfromGroup.clear()



def after_login():
    #msgcontent='传参测试/heiha'
    print('登录成功')
    namelist=['测试1111', '拳头游戏2020']
    getgname(namelist)
    #print(groupnametransfer)
    # scheduler.add_job(dataprocess.storetofile, 'cron',  day='*', hour='*', minute='*/3', second=30,
    #                   args=(msgfromGroup,))#只能传函数本身，so？
    scheduler.add_job(store, 'cron', day='*', hour='*', minute='*/3', second=30)  # 只能传函数本身，so？
    # scheduler.add_job(send_msg, 'cron', day='*', hour='*', minute='*', second=35, args=('测试1',))  # 只能传函数本身，so？
    # scheduler.add_job(send_msg, 'cron', day='*', hour='*', minute='*', second=40, args=('测试2',))  # 只能传函数本身，so？

    scheduler.start()

def after_logout():
    scheduler.shutdown()
    dataprocess.storetofile(msgfromGroup)
    print('logout')


scheduler = BackgroundScheduler()
itchat.auto_login(hotReload=True, loginCallback=after_login, exitCallback=after_logout)
#getchatroom_friendlist('测试')
itchat.run()
