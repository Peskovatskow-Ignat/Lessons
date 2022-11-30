"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""


class SpaceObject:

    def __init__(self, name, razmer):
        self.n = name
        self.raz = razmer

    def print_info(self):
        print('Имя планет -', self.n)
        print('Размер -', self.raz)


class Star(SpaceObject):

    def __init__(self, name, razmer, svetit_tip):
        super().__init__(name, razmer)
        self.svet = svetit_tip

    def svetit(self):
        print('Планета', self.n, '-',  self.svet, 'Светит')


class Planet(SpaceObject):

    def __init__(self, name, razmer, naselenie, prirost):
        super().__init__(name, razmer)
        self.nas = naselenie
        self.pri = prirost

    def svoistvo(self):
        print(self.nas, '- cвойство население планеты')

    def razmer_nas(self, old):
        self.pri = self.pri * old
        print('На', old, 'год, население соствляет', self.pri, 'Инопришленцев')


planeta = SpaceObject('Венера', str(500000000000) + 'КМ')
planeta.print_info()

planeta_svet = Star('Венера', str(500000000000) + 'КМ', 'Очень ярко')
planeta_svet.svetit()

planeta_naselenie = Planet('Венера', str(500000000000) + 'КМ', 'Не знают что такое ООП', 5000)
planeta_naselenie.svoistvo()
planeta_naselenie.razmer_nas(5)
