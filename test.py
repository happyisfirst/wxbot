#coding=utf8
import itchat, time
from apscheduler.schedulers.background import BackgroundScheduler
from itchat.content import *


#获取群聊名称，打印群聊中成员，也可修改为返回成员列表
def getchatroom_friendlist(chatroomName):
    #chatroomName='Web前端开发技术'
    itchat.get_chatrooms(update=True)

    chatrooms = itchat.search_chatrooms(name=chatroomName)

    if chatrooms:#这里是有bug的··· 改成 if chatrooms 就好了，再改了一下逻辑。
        chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
        for friend in chatroom['MemberList']:
            print('本群昵称：' + friend['DisplayName'] + '  #' '昵称:' + friend['NickName'])
            print(friend['DisplayName'] or friend['NickName'])
    else:
        print(u'没有找到群聊：' + chatroomName)

# def send_msg():
#     user_info = itchat.search_friends(name='培杰')
#     if len(user_info) > 0:
#         user_name = user_info[0]['UserName']
#         itchat.send_msg('生日快乐哦！', toUserName=user_name)


#@scheduler.scheduled_job("cron", day_of_week='*', hour='*', minute='*', second='30')
def send_msg():
        print('schedule execute')
        itchat.get_chatrooms(update=True)

        # chatrooms = itchat.search_chatrooms(name='测试')
        # chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
        # itchat.send('生日快乐哦！', chatroom['UserName'])

        chatrooms = itchat.search_chatrooms(name='测试')
       # chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
        itchat.send('定时发消息！', chatrooms[0]['UserName'])

def after_login():
    scheduler.add_job(send_msg, 'cron',  day='*', hour='*', minute='16', second=30)
    scheduler.start()

def after_logout():
    scheduler.shutdown()


# 好友信息监听--这个不是很需要
@itchat.msg_register([TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True)
def handle_friend_msg(msg):
    msg_id = msg['MsgId']
    msg_from_user = msg['User']['NickName']
    msg_content = msg['Content']
    msg_create_time = msg['CreateTime']
    msg_type = msg['Type']
    print("收到信息: ", msg_id, msg_from_user, msg_content, msg_create_time,msg_type)


# 群聊信息监听  ,需要修改成文件保存，后期再对文件数据进行加工生成报表
@itchat.msg_register([TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def information(msg):
    msg_id = msg['MsgId']
    msg_from_user = msg['ActualNickName']
    msg_content = msg['Content']
    msg_create_time = msg['CreateTime']
    msg_type = msg['Type']
    print("群聊信息: ",msg_id, msg_from_user, msg_content, msg_create_time,msg_type)


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    itchat.auto_login(hotReload=True , loginCallback=after_login , exitCallback=after_logout)
    getchatroom_friendlist('测试')
    itchat.run()
