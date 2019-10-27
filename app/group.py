import os
from app import gvariable as gl
from app.user import user

class group:

    _groupname = ''
    _members = []
    _messages = []
    _path = ''

    def __init__(self, groupname):
        self._members = []
        self._messages = []
        self._groupname = groupname
        self._path = gl.CHAT_DATA_PATH + groupname

    def processGroupContens(self):
        # 创建该群聊内容文件夹
        self.makeGroupDir()
        self.classGroupMessagesToPerson()
        self.writeTotalInfo()

    def addMessage(self,message):
        self._messages.append(message)

    def getGroupname(self):
        return self._groupname

    def getUsername(self,message):
        for index in range(len(message)):
            if(message[index] == '\t'):
                return message[:index]

    def checkUserExist(self, targetUser):
        for index in range(len(self._members)):
            if(self._members[index].getUsername() == targetUser):
                return index
        return -1

    def makeGroupDir(self):
        if(not os.path.exists(self._path)):
            os.mkdir(self._path)
            file = open(self._path + '/total.txt','w')
            file.close()

    def classGroupMessagesToPerson(self):
        ''' 将群聊信息按个人分类，归入每个用户对象中，方便后续统计 '''

        # 第一个用户
        currentUser = user(self.getUsername(self._messages[0]), self._groupname)
        self._members.append(currentUser)
        for message in self._messages:
            # 当前消息中的用户名
            message_username = self.getUsername(message)
            # 如果消息中的用户名不等于当前用户名且该用户不在member中
            if(currentUser.getUsername() != message_username 
                and (self.checkUserExist(message_username) == -1)):
                currentUser = user(message_username, self._groupname)
                self._members.append(currentUser)
            elif(currentUser.getUsername() != message_username 
                and (self.checkUserExist(message_username) >= 0)):
                currentUser = self._members[self.checkUserExist(message_username)]
            currentUser.addContent(message[len(currentUser.getUsername())+1:])
        # 将群聊信息按个人分别存入每个用户对象中
        # 接下来对每个用户群聊信息进行处理
        # for person in self._members:
        #     person.processPersonalContents()
        
    def writeTotalInfo(self):
        # 总信息文件路径
        totalFilaPath = self._path + '/total.txt'
        if(not os.path.exists(totalFilaPath)):
            file = open(totalFilaPath,'w')

        totalInfo = {}
        addedUser = []
        file = open(totalFilaPath, 'r+')
        line = file.readline()
        while line:
            if(gl.TOTAL_INFO_TITLE in line):
                line = file.readline()
                continue
            for index in range(len(line)):
                if(line[index] == ':'):
                    username = line[:index]
                    speakTimes = int(line[index+1:])
                    userIndex = self.checkUserExist(username)
                    if(userIndex > -1):
                        totalInfo[username] = speakTimes + self._members[userIndex].getContentsLength()
                        addedUser.append(userIndex)
                    else:
                        totalInfo[line[:index]] = speakTimes
                    break
            line = file.readline()
        file.close()
        file = open(totalFilaPath,'w')
        file.write(gl.TOTAL_INFO_TITLE + '\n')
        for person,times in totalInfo.items():
            file.write(person + ':' + str(times) + '\n')
        for userIndex in range(len(self._members)):
            if(userIndex in addedUser):
                continue
            file.write(self._members[userIndex].getUsername()
                 + ':'
                 + str(self._members[userIndex].getContentsLength()) + '\n')
        file.close()