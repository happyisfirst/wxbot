import itchat , time
from itchat.content import *
from apscheduler.schedulers.background import BackgroundScheduler

msgfromGroup = {}
groupName = ''

#获取群成员聊天记录。
@itchat.msg_register(TEXT, isGroupChat=True)
def text_record(msg):
    global msgfromGroup
    # if msg.isAt:
    #     msg.user.send(u'@%s\u2005I received: %s' % (msg.actualNickName, msg.text))
    print(msg.isAt)
    print('#'+msg.actualNickName+'#'+msg.text+'#'+'#')
    print(msg)
    msg_id = msg['MsgId']
    print(msg_id)
    print("########################")

#通过群名称获取群成员列表
def getchatroom_friendlist(chatroomName):
    chatroomName='拳头游戏2020校招交流群'
    itchat.get_chatrooms(update=True)
    chatrooms = itchat.search_chatrooms(name=chatroomName)

    if chatrooms:#这里是有bug的··· 改成 if chatrooms 就好了，再改了一下逻辑。
        chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
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

def after_login():
    msgcontent='传参测试/heiha'
    #scheduler.add_job(send_msg, 'cron',  day='*', hour='*', minute='*/3', second=30 ,args=(msgcontent,))#只能传函数本身，so？
    # scheduler.add_job(send_msg, 'cron', day='*', hour='*', minute='*', second=35, args=('测试1',))  # 只能传函数本身，so？
    # scheduler.add_job(send_msg, 'cron', day='*', hour='*', minute='*', second=40, args=('测试2',))  # 只能传函数本身，so？
    # scheduler.add_job(send_msg, 'cron', day='*', hour='*', minute='*', second=45, args=('测试3',))  # 只能传函数本身，so？
    # scheduler.add_job(send_msg, 'cron', day='*', hour='*', minute='*', second=55, args=('测试4',))  # 只能传函数本身，so？
    #scheduler.start()

def after_logout():
    #scheduler.shutdown()
    pass


scheduler = BackgroundScheduler()
itchat.auto_login(hotReload=True, loginCallback=after_login, exitCallback=after_logout)
#getchatroom_friendlist('测试')
itchat.run()
