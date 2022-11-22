import time
import Pazvilka

def Predlog(stroka):
    for slovo in stroka:
        print(slovo, end="", flush=True)
        time.sleep(0.03)
    print('\n')


def Podzenelie():
    Predlog('Вы начинаете вставать...')
    time.sleep(2)
    Predlog('!!!!!!!!!')
    Predlog('Вы чувствуете лёгкую дрож под ногами')
    time.sleep(2)
    Predlog('!!!')
    Predlog('Под вами проваливается земля и вы оказываетесь в пещере')
    Predlog('Вам ничего не видно')
    Predlog('В дали вы слышите громкий лай собак')
    print('1 - Сидеть тихо')
    print('2 - Идти на лай')
    Vibor = int(input('Ваш выбор - '))
    if Vibor == 1:
        Predlog('Вы сидите какое-то время но лай так и продожается')
        Predlog('Вы потихоньку встаёте и идёте вперёд...')
        time.sleep(5)
        Predlog('!!!')
        Predlog('Вы встречаете на своём пути большого огромного пса...')
        Predlog('На вид он очень злобный и страшный, однако завидив вас он успоился...')
        Predlog('Вы стоите и смотрите друг на друга...')
        Pazvilka.VIBERI_MY()
    else:
        Predlog('Вы потихоньку встаёте и идёте вперёд...')
        time.sleep(5)
        Predlog('!!!')
        Predlog('Вы встречаете на своём пути большого огромного пса...')
        Predlog('На вид он очень злобный и страшный, однако завидив вас он успоился...')
        Predlog('Вы стоите и смотрите друг на друга...')
        Pazvilka.VIBERI_MY()








def Proba():
    import time
    def Predlog(stroka):
        for slovo in stroka:
            print(slovo, end="", flush=True)
            time.sleep(0.03)
        print('\n')
    Predlog('Вы просыпаетесь от лёгкого прохладного ветра')
    Predlog('Вы видете вокруг себя множество сияющих цветов...')
    Predlog('Рядом с вами лежит ваш кинжал')
    print('1 - Отдохнуть ещё')
    print('2 - Забрать кинжал и продолжить путешествие')
    while True:
        Otvet = int(input('Выбор - '))
        if Otvet == 1:
            Predlog('Поляну в некоторой степени можно сравнить с оазисом в пустыне. Оазис дарит необходимую воду и зашиту от солнца, а поляна всегда дарит тепло, свет, тишину и уют. Место, окруженное со всех сторон деревьями, всегда кажется защищенным и умиротворенным.')
            Predlog('Вы подбираете кинжал и начинаете вставать')
            Podzenelie()
        else:
            Podzenelie()
            break