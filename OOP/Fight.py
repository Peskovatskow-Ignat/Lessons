# class Car():
#     def __init__(self, engin, color):
#         self.engin = engin
#         self.color = color
#
#     def go(self):
#         print('wrooo-wrooo')
#         print('POZA_HERO')
#
#     def print_info(self):
#         print(self.engin, self.color)
#
# Vesta = Car(1.5, 'Белый')
#
# Vesta.print_info()
# Vesta.go()
#
# print(Vesta.engin)

import time
import random


class Hero():
    def __init__(self, name, health, power, armor, weapon):
        self.n = name
        self.h = health
        self.p = power
        self.a = armor
        self.w = weapon

    def print_info(self):
        print('На поле появляется -', self.n)
        print('Этот замечательный воин имеет -', self.h, 'здоровья')
        print('С раннего детсва он дрался на улицк и поэтому его сила составляет -', self.p)
        print('На его груди великолепные доспехи с характиристиками -', self.a, 'брони')
        print('В его руках мы можем видеть -', self.w)

    def strike(self, Ignat):
        print(
            '-> ⚔  ' + self.n + ' 🤼 ' + Ignat.n + 'a', 'Используя  ' + self.w + '🍾')
        time.sleep(2)
        print('-> 🛡️  ' + Ignat.n + '  Смог защититься и у него осталось  ' + str(Ignat.h - self.p + Ignat.a) + '❤')
        Ignat.h = Ignat.h - self.p + Ignat.a

    def strike_1(self, Vitalik):
        print(
            '-> ⚔  ' + self.n + ' 🤫 ' + Vitalik.n + 'a', 'Используя  ' + self.w + '🐑')
        time.sleep(2)
        print('-> 🛡️  ' + Vitalik.n, '  Смог защититься и у него осталось  ', str(Vitalik.h - self.p + Vitalik.a) + '❤')
        Vitalik.h = Vitalik.h - self.p + Vitalik.a


Vitalik = Hero('Виталик', random.randint(2500, 10000), random.randint(500, 1500), random.randint(100, 250), 'Самодельную розочку')
Ignat = Hero('Игнат', random.randint(2500, 10000), random.randint(500, 1500), random.randint(100, 250), 'Ягнят')
while True:
    Vitalik.strike(Ignat)
    print('Время отвтеа', Ignat.n, ' 👊 ', Vitalik.n)
    time.sleep(2)
    Ignat.strike_1(Vitalik)
    if Vitalik.h <= 0:
        print(Vitalik.n, ' Потерпел поражение😢')
        print(Ignat.h, '❤  Осталось у победителя')
        break
    elif Ignat.h <= 0:
        print(Ignat.n, ' Потерпел поражение😢')
        print(Vitalik.h, '❤  Осталось у победителя')
        break
    else:
        print('Ну что новый раунд???')
        time.sleep(2)
        print('̿̿ ̿̿ ̿̿ ̿̿\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/̿̿ ̿ ̿̿ ̿̿ ̿̿')
        time.sleep(1)
