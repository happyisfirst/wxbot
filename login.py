import itchat , time
from itchat.content import *

# @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
# def text_reply(msg):
#     msg.user.send('%s' % msg.text)

# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO]) # 可以将群聊中的图片语音小视频发送记录保存到日志。
# def download_files(msg):
#     msg.download(msg.fileName)
#     typeSymbol = {
#         PICTURE: 'img',
#         VIDEO: 'vid', }.get(msg.type, 'fil')
#     return '@%s@%s' % (typeSymbol, msg.fileName)

# @itchat.msg_register(FRIENDS)
# def add_friend(msg):
#     msg.user.verify()
#     msg.user.send('Nice to meet you!')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))
    print(msg.isAt)
    print(msg.actualNickName)
    print(msg.text)


itchat.auto_login(hotReload=True)

# print('here')
# chatroomlist=itchat.get_chatrooms()
# memberList = itchat.update_chatroom(name='测试', detailedMember=True)
# print(memberList)


memberList = itchat.get_friends()[1:5]
print(memberList)
# 创建群聊，topic键值为群聊名
chatroomUserName = itchat.create_chatroom(memberList, 'test chatroom')
# 删除群聊内的用户
#itchat.delete_member_from_chatroom(chatroomUserName, memberList[0])
# 增加用户进入群聊
itchat.add_member_into_chatroom(chatroomUserName, memberList[0], useInvitation=False)

itchat.run(True)

