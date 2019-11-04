import os
'''
全局变量文件
用于存储全局变量
'''
# 文件夹信息文件的文件名
TOTAL_INFO_FILE = 'total.txt'
# 信息文件的头
TOTAL_INFO_TITLE = u'目前为止用户总发言次数:'
TOTAL_KEYINFO_TITLE = u'目前为止用户关键词发言次数:'

# 路径分隔符
PATH_SEPARATOR = u'/'

# 聊天文件存储路径
#CHAT_DATA_PATH=os.getcwd() + '/data/'
CHAT_DATA_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + PATH_SEPARATOR + 'data' + PATH_SEPARATOR

# 聊天信息存储文件名
CHATFILE_FILENAME = 'groupmsg.txt'
# 群成员列表文件
FRIENDLIST_TFILE = 'groupmember.txt'
# 群消息暂存
CHATFILE_TEMP_FILENAME = 'tempgroupmsg.txt'

GROUP_KEYS = {}
GROUP_NAMELIST =[]