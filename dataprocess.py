import time
import os


def storetofile(groupname, msglist):
    # filename = os.getcwd() +'/data/'+ time.strftime("%Y-%m-%d", time.localtime()) + '.txt'  #存储到data 目录下
    filename = os.getcwd() + '/data/' + groupname + '.txt'  # 用groupname为文件名存储到data 目录下
    f = open(filename, 'a')
    for msg in msglist:
        f.write(msg)
    f.close()


# 读取文件并对
def proecssdata(groupname):
    filename = os.getcwd() + '/data/' + groupname + '.txt'
    f = open(filename, 'r')
    content = f.readlines()  # 读取文件中的全部行，按行划分存储到列表中，类型字符串


# 对一行聊天记录进行分解，读取必要信息
def processline(msgcontent):
    pass


class Record:
    count = 0  # 每100个记录就进行一次存储

    def __init__(self):
        self.msgDic = {}

    # def storeToFileExit(self):
    #     filename = time.strftime("%Y-%m-%d", time.localtime()) + '.txt'
    #     f = open(filename, 'a')
    #     for msg in self.msgList:
    #         f.write(msg)
    #     f.close()
    #     self.msgList = []
    #     self.count = 0

