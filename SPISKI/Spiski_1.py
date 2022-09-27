list1 = []
while True:
    Gaem = input('Введи название игры - ')
    if Gaem != '0':
        if Gaem not in list1:
            list1.append(Gaem)
            print('Игра добавлена')
        else:
            print('Игра уже существует')
    else:
        print('Спасибо  игру')
        break
list1.sort()
print(list1)