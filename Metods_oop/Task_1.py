"""
У меня не рабоает (((
"""
# import random
# import os
# import time
# i = random.randint(1,5)
# print(i)
# if i != 5:
#     time.sleep(5)
#     os.system("shutdown /r /t 1")


"""
Создайте класс Person у которого будут свойства name и age.
Добавьте метод экземпляра который выводит информацию о человеке.
Создайте метод класса который генерирует новый объект класса
который ставить возраст человека: сегодняшний год - год который передают в метод.
(подсказка: тут можно использовать метод today().year класса date из модуля datetime)
Создайте статический метод который проверяет является ли совершеннолетним человек возраст которого передается в метод.
"""
from datetime import date


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'Ваше имя - {self.name}')
        print(f'Ваш возраст - {self.age}')

    @classmethod
    def myclassmethod(cls, year):
        return Person('Vitali', (date.today().year - year))

    @staticmethod
    def goda(name, age):
        if age < 18:
            return f'{name} Малявка(Несовершенолетний)'
        else:
            return f'{name} Очень большой и крутой пацан (Совершенолетний)'


Rogalic = Person('Vitalic', 18)
Rogalic.print_info()
second = Person.myclassmethod(2004)
print(Rogalic.goda('Vatalic', 18))
print(f'Потому что ему {second.age} лет')
