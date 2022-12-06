"""
Создать базовый класс ОЛИМПИАДНЫЕ ЗАДАНИЯ (данные об участнике, количество тестовых примеров,
количество пройденных тестов).
Создать производные классы ЗАДАНИЯ «ВСЕ ИЛИ НИЧЕГО»
(задается максимальное количество баллов за задание (даются только когда все тесты пройдены)
и ЗАДАНИЯ «ЧЕМ БЫСТРЕЕ, ТЕМ ЛУЧШЕ» (задается время участника на решение,
лучшее время всех участников, максимальное количество баллов за задание,
процент снижения балла в минуту отставания от лучшего времени).
Для заданных примеров задач, которые решали участники,
упорядочить участников по росту набранных баллов и определить суммарное количество баллов,
набранных заданным участником олимпиады.
Для проверки использовать действия над списком,
в котором разместить объекты разных производных классов.
"""

class Olimp_zadanie:

    def __init__(self, name, tests, tests_trye):
        self.name = name
        self.t = tests
        self.tt = tests_trye

class Vso_ili_nichego(Olimp_zadanie):

    def __init__(self, name, tests, tests_trye, good, ne_good):
        super().__init__(name, tests, tests_trye)
        self.g = good
        self.ng = ne_good

class Bistro(Olimp_zadanie):

    def __init__(self, name, tests, tests_trye, time_1, time_good, max_ball, prochent_time):
        super().__init__(name, tests, tests_trye)
        self.time_resh = time_1
        self.good_t = time_good
        self.ball_m = max_ball
        self.otstal = prochent_time


igor = Vso_ili_nichego('Игарёк', 16, 7, 9, 3)
bagrat = Vso_ili_nichego('Багратик', 99, 16, 8, 8)
makson = Vso_ili_nichego('Братик багартик', 99, 16, 10, 6)

Shasha = Bistro('Сашка Шляпа', 67, 15, 3, 15, 5, 3)
Shasha_T = Bistro('Сашка Труба', 67, 15, 8, 15, 99, 9)
Shasha_P = Bistro('Сашка Полицай', 67, 15, 14, 15, 7, 0)

mama = {}

max_ball = 0
for i in [igor, bagrat, makson]:
    max_ball += i.g
print(f'Максимальный балл - {max_ball} в дисциплине "Всё или ничего"')
for i in [igor, bagrat, makson]:
    mama[i.g] = i.name

# print(mama)
mama = dict(sorted(mama.items()))
# print(mama)
for i, j in enumerate(list(mama.values())):
    print(f'{i+1} Место - {j}')
mama = {}
for i in [Shasha, Shasha_P, Shasha_T]:
    mama[i.ball_m] = i.name

mama = dict(sorted(mama.items()))
max_ball = 0
for i in [Shasha, Shasha_P, Shasha_T]:
    max_ball += i.ball_m
print(f'Максимальный балл - {max_ball} в дисциплине "Чем быстрее тем лучше"')
for i, j in enumerate(list(mama.values())):
    print(f'{i+1} Место - {j}')
