Kategory = input('Категория - ')
Kategory = Kategory.lower()
if Kategory == 'продукты':
    Summa = input('Цена - ')
    if Kategory in range(0, 100):
        print('Попробуйте нашу выпечку')
    elif Kategory in range(100, 500):
        print('Как насчёторехов в шоколаде')
    else:
        print('Попробуйте экзотческие фрукты')
else:
    print('Загляните в товары для дома')