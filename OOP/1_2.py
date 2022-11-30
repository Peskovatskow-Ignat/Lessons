class Prymoygolnik():
    def __init__(self, dlina, shirina):
        self.d = dlina
        self.s = shirina

    def info(self):
        print('Прямоугольник имее длинну', self.d, 'см')
        print('Прямоугольник имее ширину', self.s, 'см')

    def perimetr(self):
        return self.d + self.d + self.s + self.s

    def Ploshed(self):
        return self.d * self.s


prymoi = Prymoygolnik(4, 2)

prymoi.info()

print(prymoi.perimetr(), prymoi.Ploshed())