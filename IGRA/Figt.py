from random import *
from time import *
def Predlog(stroka):
    for slovo in stroka:
        print(slovo, end="", flush=True)
        sleep(0.03)
    print('\n')

class Game():
    def __init__(self, hp=1000, hp_enemy=2000,):
        self.hp = hp
        self.hp_1 = hp_enemy
        while True:
            print('Выберите действие, указав число\n1)"удар!!!"\n2)"Cкушать пряник"')
            hit = int(input('Выбор - '))
            if hit == 1:
                b = randint(200, 500)
                self.hp_1 -= b
                print('У кикиморы осталось ', self.hp_1, 'hp')
                sleep(1)
                print('Собакен бьет вас левой лапой')
                sleep(1)
                c = randint(100, 300)
                self.hp -= c
                print('У вас осталось', self.hp, 'hp')
                sleep(1)
            if hit == 2 and self.hp < 1000:
                if self.hp > 100:
                    self.hp += randint(100, 260)
                    print('Ваше хп - ', self.hp)
                    sleep(1)
                else:
                    self.hp += randint(500, 600)
                    print('Ваше хп - ', self.hp)
                    sleep(1)
            if self.hp <= 0:
                print(
                    '''
            ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
            ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
            ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
            ██▌░│██████▌░░░▐██████│░▐██
            ███░│▐███▀▀░░▄░░▀▀███▌│░███
            ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
            ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
            ████▄─┘██▌░░░░░░░▐██└─▄████
            █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
            ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
            █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
                    ''')
                exit()
            if self.hp_1 <= 0:
                print('Вы выйграли')
                Predlog('Однако после боя вы замечаете сильное кровотечение в районе живота живота')
                Predlog('Вы медленно ложипесь на холодный камень и уходите в мир иной с мыслью что эта тварь никогда больше не потревожт простой народ...')
                Predlog(
                '''
░░░░░░░░░░░░░██
░░░░░░░░░░░░█░░█
░░░░░░░░░░░░█░░█
░░░░░░░░░░░█░░░█
░░░░░░░░░░█░░░░█
████████▄▄█░░░░░███████████▄
▓▓▓▓▓▓▓█░░░░░░░░░░░░░░░░░░░█
▓▓▓▓▓▓▓█░░█░░░█▀█░█▀▀░█▀█░░░█
▓▓▓▓▓▓▓█▀▀█▀▀░█▀▄░█▀░░█▀▀░░░█
▓▓▓▓▓▓▓█░░█░░░▀░▀░▀▀▀░▀░░░░█
▓▓▓▓▓▓▓█░░░░░░░░░░░░░░░░░░█
▓▓▓▓▓▓▓█████░░░░░░░░░░░░░█
███████▀░░░░▀▀██████████▀
                ''')
                exit()