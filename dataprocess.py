import time
import os

# 后期可以改善创建一个文件夹去存
def storetofile(msglist):

    if msglist ==[]:
        print('空')
        return
    #f ilename = os.getcwd() + '/data/groupmsg.txt'  # 用groupname为文件名存储到data 目录下
    filename='groupmsg.txt'
    basedir = os.path.dirname(__file__)

    # 如果没有创建目录
    isExists = os.path.exists(basedir + '/data')
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(basedir + '/data')

    file_path = os.path.join(basedir, './data', filename)
    f = open(file_path, 'a')
    for msg in msglist:
        f.write(msg+'\n')
    f.close()
    print('存储成功，时间：'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

def storetotempfile(msglist):
    #f ilename = os.getcwd() + '/data/groupmsg.txt'  # 用groupname为文件名存储到data 目录下
    if msglist ==[]:
        print('空')
        return
    filename='tempgroupmsg.txt'
    f = open(filename, 'w')
    for msg in msglist:
        f.write(msg+'\n')
    f.close()
    #print('存储成功，时间：'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# # 读取文件并对数据进行解析
# def proecssdata():
#     filename = os.getcwd() + '/data/groupmsg.txt'
#     f = open(filename, 'r')
#     content = f.readlines()  # 读取文件中的全部行，按行划分存储到列表中，类型字符串
#     variable=processline(content)


# # 读取配置文件，进行程序初始化
# def readconfigfile():
#     filename = os.getcwd() + '/data/groupmsg.txt'
#     f = open(filename, 'r')
#     content = f.readlines()  # 读取文件中的全部行，按行划分存储到列表中，类型字符串
#     variable=processline(content)
#
#
# # 对一行聊天记录进行分解，读取必要信息
# def processline(msgcontent):
#     variable = []
#     return variable


# def getkeyword(lines):
#     #读取配置文件
#     return {'测试1111': ['打卡', '测试', '签到'], '拳头游戏2020': ['1', '签到', '早']}

def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]


