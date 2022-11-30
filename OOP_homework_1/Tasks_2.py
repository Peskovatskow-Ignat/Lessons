"""
Создайте класс который будет устанавливать свойство name и иметь метод
который к имени прибавляет надпись "гений". Создайте еще 1 класс, унаследуйте предыдущий.
Во втором классе вызовите метод класса родителя и добавьте к выводу надпись "но его отчислят если он не будет учить ООП"
Создайте экземпляр второго класса с вашим именем и вызовите метод печатающий всю надпись.
"""
import time


class Name:

    def __init__(self, name):
        self.n = name

    def print_info(self):
        print('На сценееее ', end='')
        time.sleep(1)
        print('На сценееее ', end='')
        time.sleep(2)
        print(self.n, 'и он гений')


class Otchislenie(Name):

    def poka(self):
        super().print_info()
        time.sleep(1)
        print('Но', self.n, 'отчиcлят и он не будет учить OOП')


Ignat = Otchislenie('Игнат')
Ignat.poka()
