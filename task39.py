import io


fileName = 'tel.txt'


def main_menu():
    print('''
     Введите номер действия:
1 - Показать все записи
2 - Найти запись по вхождению частей имени
3 - Найти запись по телефону
4 - Добавить новый контакт
5 - Удалить контакт
6 - Изменить номер телефона у контакта
7 - Выход''')
    print()
    return input('Введите номер действия: ')


def writeFile(fileName):
    with open(fileName, 'w') as data:
        data.writelines(" " + '\n')


def readFile(fileName):
    result = []
    with open(fileName, 'r') as data:
        for line in data:
            result.append(line.split()) 
    return result


def showTelBook(fileName):
    userList = readFile(fileName)
    for num, line in enumerate(userList):
        print(f'{num+1}) {line[0]} {line[1]} {line[2]} {line[3]}')



def findUsers(fileName):
    userList = readFile(fileName)
    request = input('Введите имя: ').capitalize()
    for user in userList:
        if request in user[0] or request in user[1] or request in user[2]:
            print(f'{user[0]} {user[1]} {user[2]} {user[3]}')


def findNumTel(fileName):
    userList = readFile(fileName)
    request = input('Введите номер телефона: ').capitalize()
    for user in userList:
        if request in user[3]:
            print(f'{user[3]}: {user[0]} {user[1]} {user[2]}')


def addUser(fileName):
    contact = []

with io.open(fileName, 'a') as f:
        f.write('\n'+ 'Galkin, Oleg, Olegovich, +123456')
        print('Новый контакт добавлен')


def deleteUser(userList):
    userList = readFile(fileName)
    for num, line in enumerate(userList):
        print(f'{num+1}) {line[0]} {line[1]} {line[2]} {line[3]}')
    print()
    lineDel = int(input('Введите номер строки для удаления контакта: '))
    deleteUser = userList.pop(lineDel - 1)
    print(f'Контакт {deleteUser[0]} {deleteUser[1]} {deleteUser[2]} удален')
    writeFile(userList)


def changeNumTel(fileName):
    userList = readFile(fileName)
    contactChange = input('Фамилия контакта для изменения номера телефона: ').capitalize()
    for i, contact in enumerate(userList):
        if i[0] == contactChange:
                new_number = input('Введите новый номер: ')
                userList[i][3] = new_number
                print('Номер телефона изменен')
        else:
                print()
    writeFile(userList)

run = True

mode = main_menu()
if mode == '1':
        showTelBook(fileName)
        print()
        input('Нажмите Enter, чтобы вернуться в меню')
elif mode == '2':
        findUsers(fileName)
        print()
        input('Нажмите Enter, чтобы вернуться в меню')
elif mode == '3':
       findNumTel(fileName)
       print()
       input('Нажмите Enter, чтобы вернуться в меню')
elif mode == '4':
        addUser(fileName)
        print()
        input('Нажмите Enter, чтобы вернуться в меню')
elif mode == '5':
        deleteUser(readFile(fileName))
elif mode == '6':
        changeNumTel(fileName)
        print()
        input('Нажмите Enter, чтобы вернуться в меню')
elif mode == '7':
        print()
        print('Выход')
        run = False
else:
       print()
       input('Нажмите Enter, чтобы вернуться в меню')
