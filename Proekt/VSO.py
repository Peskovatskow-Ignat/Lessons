import Paspisanie
import prise
import information
import Test_Na_fermera
import Gadalka
list1 = ['Расписание Занятий', 'Продукция', 'Информация о людях', 'Тест на фермера', 'Гадалка']
# print('Наш сервис предлагает узнать следующие категории:')
# print('------------------------------------------------------------------------------------------------------------')
# for i in list1:
#     print('+', i)
# print('------------------------------------------------------------------------------------------------------------')
# vibor = input('Напишете название категории которая вас интересует - ')
# vibor = vibor.lower()

while True:
    print('-' * 108)
    print('Вы попали в село Любимкмно! тут вы можете увитель следующие прикалюхи!')
    print(
        '------------------------------------------------------------------------------------------------------------')
    for i in list1:
        print('+', i)
    print(
        '------------------------------------------------------------------------------------------------------------')
    vibor = input('Напишете название категории которая вас интересует - ')
    vibor = vibor.lower()

    if 'сп' in vibor:
        Paspisanie.Raspisanie()
    elif 'пр' in vibor:
        prise.Price()
    elif 'нф' in vibor:
        information.INF()
    elif 'тес' in vibor:
        Test_Na_fermera.test()
    elif 'лк' in vibor or 'гад' in vibor:
        Gadalka.next1()
    else:
        print('Я ваш Английский не понимать (переформулируйте запрос)')
    input('введите enter чтобы продолжить')

