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

Vixod = ['Молча пешочком🚶', 'Бегом из Siriusa🏃‍', 'Бегом из пятёрочки🤸‍', 'Верхом на коне🏇']

weapon = ['Булову🧷', 'Лук🏹', 'Мячь⚽', 'Розочку из бутылки🍾', 'Палку убивалку🏏', 'Деньги💲', 'Люгушку🐸', 'Друга маминой подруги🤵']


vid = ['Большой бицепс💪', 'Бороду колдуна🧙','Маску клоуна🤡']
vibor_1 = random.choice(vid)
vibor_2 = random.choice(vid)
class Hero():
    def __init__(self, name, health, power, armor, weapon):
        self.n = name
        self.h = health
        self.p = power
        self.a = armor
        self.w = weapon

    def print_info(self):
        print(random.choice(Vixod))
        print('На поле появляется -', self.n)
        print('Этот замечательный воин имеет -', self.h, 'здоровья')
        print('С раннего детсва он дрался на улицк и поэтому его сила составляет -', self.p)
        print('На его груди великолепные доспехи с характиристиками -', self.a, 'брони')
        print('Глядя на него можно увидеть -', self.w)
        print('-' * 108)

    def strike(self, Ignat):
        print(
            '-> ⚔  ' + self.n + ' 🤼 ' + Ignat.n + 'a', 'Используя  ' + random.choice(weapon))
        time.sleep(2)
        print('-> 🛡️  ' + Ignat.n + '  Смог защититься и у него осталось  ' + str(Ignat.h - self.p + Ignat.a) + '❤')
        Ignat.h = Ignat.h - self.p + Ignat.a

    def strike_1(self, Vitalik):
        print(
            '-> ⚔  ' + self.n + ' 🤫 ' + Vitalik.n + 'a', 'Используя  ' + random.choice(weapon))
        time.sleep(2)
        print('-> 🛡️  ' + Vitalik.n, '  Смог защититься и у него осталось  ', str(Vitalik.h - self.p + Vitalik.a) + '❤')
        Vitalik.h = Vitalik.h - self.p + Vitalik.a
    def strike_Magik(self, Ignat):
        print(
            '-> ⚔  ' + self.n + ' 👊 ' + Ignat.n + 'a', 'Используя ' + random.choice(weapon))
        time.sleep(2)
        print('-> 🛡️  ' + Ignat.n + '  Смог защититься и у него осталось  ' + str(Ignat.h - self.p + Ignat.a) + '❤')
        Ignat.h = Ignat.h - self.p + Ignat.a
        print('-' * 108)

class Warrior(Hero):  # Создание класса наследника
    def __init__(self, name, health, power, armor, weapon, name_2):
        super().__init__(name, health, power, armor, weapon)
        self.n_2 = name_2

    def hello(self):  # Приветсвие
        super().print_info()

    def ataka_Igant(self, Ignat):  # Атака
        super().strike_Magik(Ignat)



Vitalik = Hero('Виталик', random.randint(2500, 10000), random.randint(500, 1500), random.randint(100, 250),random.choice(vid))
Magician = Warrior('Магикян', random.randint(2500, 10000), random.randint(500, 1500), random.randint(100, 250), random.choice(vid), 13)
Ignat = Hero('Игнат', random.randint(2500, 10000), random.randint(500, 1500), random.randint(100, 250), random.choice(vid))

Vitalik.print_info()
time.sleep(2)
Magician.hello()
time.sleep(1)
Magician.ataka_Igant(Ignat)
time.sleep(1)
Ignat.strike_Magik(Magician)


# while True:
#     Vitalik.strike(Ignat)
#     print('Время отвтеа', Ignat.n, ' 👊 ', Vitalik.n)
#     time.sleep(2)
#     Ignat.strike_1(Vitalik)
#     if Vitalik.h <= 0:
#         print(Vitalik.n, ' Потерпел поражение😢')
#         print(Ignat.h, '❤  Осталось у победителя')
#         break
#     elif Ignat.h <= 0:
#         print(Ignat.n, ' Потерпел поражение😢')
#         print(Vitalik.h, '❤  Осталось у победителя')
#         break
#     else:
#         print('Ну что новый раунд???')
#         time.sleep(2)
#         print('̿̿ ̿̿ ̿̿ ̿̿\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/̿̿ ̿ ̿̿ ̿̿ ̿̿')
#         time.sleep(1)