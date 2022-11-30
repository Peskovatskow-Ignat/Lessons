class Bus():
    def __init__(self, speed, capacity, max_speed, emptyseats):
        self.speed = speed
        self.capacity = capacity
        self.max_s = max_speed
        self.empt = emptyseats

    def Posadka(self, kol_vo):
        if self.empt >= kol_vo:
            self.empt -= kol_vo
            print('Посадили -', kol_vo)
            print('Осталось -', self.empt)
        else:
            print('Посадили', self.empt)
            print('Свободных мест нет')
            self.empt = 0
    def Razognatsya(self, speed):
        if speed + self.speed < self.max_s:
            print('Разогнались до', self.speed + speed)
            self.speed += speed
        else:
            print('Едем в село с мах. скоростью - ', self.max_s)
            self.speed = self.max_s

Aftobys = Bus(40, 80, 200, 40)

Aftobys.Posadka(5)
Aftobys.Posadka(65)
Aftobys.Razognatsya(150)
Aftobys.Razognatsya(50)

