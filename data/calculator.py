import os
import time
import datetime
import gvariable as gl

def calculateUserSpeakingTimes(groupname, username, start, end):

    '''
    在指定群聊内查找特定用户在特定时间段的发言
    @para groupname ： 要找的目标群聊
    @para username ： 所要找的特定用户
    @para start ： 查找聊天的开始时间点
    @para end ： 查找聊天的结束时间点
    @return contents : 该时间段该用户的发言记录
    '''

    filepath = gl.CHAT_DATA_PATH + groupname + gl.PATH_SEPARATOR + username
    if(not os.path.exists(filepath)):
        print('该用户或群聊不存在！')
        return
    file = open(filepath, 'r')
    startTime = strToTime(start)
    endTime = strToTime(end)
    contents = []
    line = file.readline()
    while line:
        # 从每行获取时间戳
        speakTime = strToTime(line[-20:-1])
        beginFlag = int(startTime) - int(speakTime)
        endFlag = int(speakTime) - int(endTime)
        if(beginFlag <= 0 and endFlag <= 0):
            contents.append(line[:-21])
        elif(endFlag > 0):
            break
        line = file.readline()
    file.close()
    return contents


def getDatetime(content):
    # 从字符串中分割出时间字符串
    for index in range(len(content)):
        if(content[index] == '\t'):
            return time.strptime(content[index:],"%Y-%m-%d %H-%M-%S")


def strToTime(str):
    # 将时间字符串转换为秒
    return time.mktime(time.strptime(str, '%Y-%m-%d %H:%M:%S'))


def calculateKeywordTimes(groupname, keyword, start, end):
    '''
    在指定群聊内统计所有用户关键词出现次数
    @para groupname ： 要找的目标群聊
    @para keyword : 所要找的特定关键词
    @para start ： 查找聊天的开始时间点
    @para end ： 查找聊天的结束时间点
    @return len ： 消息条数
    '''
    filepath = gl.CHAT_DATA_PATH + groupname
    files = os.listdir(filepath)
    result = {}
    for file in files:
        if(gl.TOTAL_INFO_FILE in file):
            continue
        contents = calculateUserSpeakingTimes(groupname, file, start, end)
        keywordTimes = 0
        for content in contents:
            if(keyword in content):
                keywordTimes = keywordTimes + 1
        result[file] = keywordTimes
    return result