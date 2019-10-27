import os
import gvariable as gl
from calculator import *

class user:

    _username = ''
    _contents = []
    _path = ''
    _group = ''

    
    def __init__(self, username, groupname):
        self._username = username
        self._contents = []
        self._group = groupname
        self._path = gl.CHAT_DATA_PATH + groupname + gl.PATH_SEPARATOR + username

    def processPersonalContents(self):
        # self.makePersonFile()
        # self.storeContents()
        # calculateUserSpeakingTimes(
        #     self._group, 
        #     self._username,
        #     '2019-10-24 21:14:00',
        #     '2019-10-24 21:15:00')

        calculateKeywordTimes(
            self._group, 
            '哈哈',
            '2019-10-24 21:14:00',
            '2019-10-24 21:18:00')
    def getUsername(self):
        return self._username

    def addContent(self, content):
        self._contents.append(content)
    
    def makePersonFile(self):
        if(not os.path.exists(self._path)):
            os.mknod(self._path)

    def storeContents(self):
        if(self._username[0] != '一'):
            return
        file = open(self._path, 'a')
        for content in self._contents:
            file.write(content + '\n')
        file.close()

    def calculateSpeakingTimes(self):
        calculateUserSpeakingTimes(
            self._group, 
            self._username,
            '2019-10-24 21:14:00',
            '2019-10-24 21:15:00')
        
        calculateKeywordTimes(
            self._group, 
            '哈哈',
            '2019-10-24 21:14:00',
            '2019-10-24 21:18:00')

    def getContentsLength(self):
        return len(self._contents)