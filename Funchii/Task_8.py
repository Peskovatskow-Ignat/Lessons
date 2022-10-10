"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.
Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""


def caluate(n):
    Sred = 0
    Slovar = {}
    list1 = []
    list2 = []
    m = 0
    if n == 'off':
        return print('End')
    elif n == 'Start':
        privet_Oleg = int(input('Введите количество цифр - '))
        for i in range(privet_Oleg):
            Poka_Oleg = int(input('Введите число - '))
            Sred = Sred + Poka_Oleg
            list1.append(Poka_Oleg)
            m += 1
        Sred /= m
        for x in list1:
            if x > Sred:
                Slovar[Sred] = x
            else:
                list2.append(x)
        print('Значения меньше среднего -', list2)
        print(Slovar)

caluate(n = input('(Star/off) - '))

