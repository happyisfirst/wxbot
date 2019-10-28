import time
import os
from app import gvariable as gl
from app.fileprocess import classMessageByGroup
# 将所有聊天记录存放到这里
def storetofile(msglist):
    # 如果聊天列表为空，直接退出函数
    if not msglist:
        return
    # 用groupname为文件名存储到data 目录下
    filename = gl.CHAT_DATA_PATH + gl.CHATFILE_FILENAME
    f = open(filename, 'a')
    for msg in msglist:
        f.write(msg+'\n')
    f.close()
    print('存储成功，时间：'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 暂存聊天记录以供数据分析使用
def storetotempfile(msglist):
    # 如果聊天列表为空，直接退出函数,会导致重复统计
    # if not msglist:
    #     return
    filename = gl.CHAT_DATA_PATH + gl.CHATFILE_TEMP_FILENAME
    f = open(filename, 'w')
    for msg in msglist:
        f.write(msg+'\n')
    f.close()

# 生成数据存放的目录
def createdatadir():
    isExists = os.path.exists(gl.CHAT_DATA_PATH)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(gl.CHAT_DATA_PATH)
        print('create data dir successfully')

# 通过值返回键值
def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]

def statictempfile():
    classMessageByGroup()

