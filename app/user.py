from app.calculator import *
import datetime

class user:

    _username = u''
    _contents = []
    _path = u''
    _group = u''
    _groupkeys= []

    
    def __init__(self, username, groupname, groupkeys):
        self._username = username
        self._contents = []
        self._group = groupname
        self._path = gl.CHAT_DATA_PATH + groupname + gl.PATH_SEPARATOR + username
        self._groupkeys = groupkeys

    def processPersonalContents(self):

        self.makePersonFile()
        # 计算日期间隔
        now=datetime.datetime.now()
        endtime=now.strftime('%Y-%m-%d %H:%M:%S')
        delta = datetime.timedelta(days=7)
        begintime=(now - delta).strftime('%Y-%m-%d %H:%M:%S')

        calculateKeywordTimes(
            self._group, 
            self._groupkeys,
            begintime,
            endtime)
       # print('processpersonalcontents')


        self.writepersonInfo()

    def getUsername(self):
        return self._username

    def addContent(self, content):
        self._contents.append(content)
    
    def makePersonFile(self):
        if(not os.path.exists(self._path)):
            file = open(self._path, 'w')
            file.close()

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
            '2019-10-28 12:14:00',
            '2019-10-28 21:15:00')
        
        calculateKeywordTimes(
            self._group, 
            self._groupkeys,
            '2019-10-28 12:14:00',
            '2019-10-28 21:18:00')

    def getContentsLength(self):
        return len(self._contents)

    def getkeysnumInfo(self, keywords):
        count= 0
        for line in self._contents:
            line = line[:-20]
            for keyword in keywords:
                if keyword in line:
                    count = count+1
                    break

        return count


