from app import gvariable as gl
from app.group import group
def classMessageByGroup():
    filename = gl.CHAT_DATA_PATH + gl.CHATFILE_TEMP_FILENAME
    try:
        file_handler = open(filename, mode='r')
    except IOError:
        print('no such file')
        file_handler.close()
        return

    content = file_handler.readline()
    if content=='':
        return

    groupname = getGroupName(content)

    currentgroup = group(groupname, gl.GROUP_KEYS[groupname])
    while content:
        if(content == '\n'):
            content = file_handler.readline()
            continue
        if(currentgroup.getGroupname() != getGroupName(content)):
            # 处理下一个群聊内容
            currentgroup.processGroupContens()
            groupname = getGroupName(content)
            currentgroup = group(groupname, gl.GROUP_KEYS[groupname])

        currentgroup.addMessage(content[len(currentgroup.getGroupname())+1:])
        #print(content[len(groupname)+1:])
        content = file_handler.readline()
    currentgroup.processGroupContens()
    file_handler.close()

def getGroupName(message):
    for index in range(len(message)):
        if(message[index] == '\t'):
            return message[:index]


