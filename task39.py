fileName = 'tel.txt'


def writeFile(fileName):
    with open(fileName, 'a') as data:
        data.writelines("Hello world" + '\n')


def readFile(fileName):
    result = []
    with open(fileName, 'r+') as data:
        for line in data:
            result.append(line.split()) 
    return result

def findUsers(userList):
    name = 'Ivan,'

    for user in userList:
      if user[1] == name:
        print(user[3])


#writeFile(fileName)
print(type(readFile(fileName)))
print(readFile(fileName))
findUsers(readFile(fileName))
