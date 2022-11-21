import time
import Home
import sys
import Prikol

print(
'''
●▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬●
‎‎‎‎‎‎‎‎░░░░░░░░░░░░░░░ДОБРО ПОЖАЛОВАТЬ ░░░░░░░░░░░░░░
‎‎‎‎‎‎‎‎‎‎‎‎●▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬●
''')

def Menu():
    print('Хотите узнать больше о нашей игре - 1')
    print('Подсказка по игре - 2')
    print('Узнать разработсиков -3')
    print('Начать игру - 4')
    Vibor = int(input('Ваш выбор - '))
    return Vibor


Vibor = Menu()


while True:
    if Vibor == 1:
        print('Наша история про одну замечательную девочку Анюту которая любила увлекаться боевыми искуствами. И однажды она решила отправиться в путешевствие... ')
        time.sleep(2)
        print('Давайте посмотрим что из этого вышло!!!')
        time.sleep(3)
        Vibor = Menu()
    elif Vibor == 2:
        print('Игра текстовая и очень лёгкая ты разберёшься!')
        time.sleep(3)
        Vibor = Menu()
    elif Vibor == 3:
        print('Будникова Софья')
        print('Песковацков Игнат')
        time.sleep(3)
        Vibor = Menu()
    else:
        print('Начнём игру')
        Prikol.Loading()
        Home.Proba()
        break