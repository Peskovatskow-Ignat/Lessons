def next1():
    import random
    slovo =""
    while not  ("наз" in slovo) :
        print('------------------------------------------------------------------------------------------------------------')
        list1 = ['Уражай', 'Любовь', 'Дети', 'Будующее']
        print('Ты пришёл к гадалке')
        print('На что будем гадать? ')
        for i in list1:
            print('-', i)
            rand = random.randint(0, 100)
        slovo = input('Введите категорию - ')

        print('-' * 108)
        slovo = slovo.lower()
        if 'ур' in slovo:
            if rand in range(0, 34):
                print('Уражай будет плохой')
            elif rand in range(34,67):
                print('Урожай будет плохой... до следуего года хватит')
            elif rand in range(67, 101):
                print('Уражая будет завались!')
            print('-' * 108)

        if 'люб' in slovo:
            if rand in range(0, 34):
                print('Ты проживёшь в одиночестве')
            elif rand in range(34,67):
                print('Найдёшь любовь но вы растанетесь')
            elif rand in range(67, 101):
                print('У тебя будет самая лучшая девушка в мире!')
            print('-' * 108)

        elif 'дет' in slovo:
            if rand in range(0, 34):
                print('Детей небудет')
            elif rand in range(34,67):
                print('Детей будет больше 20 (ШОК)')
            elif rand in range(67, 101):
                print('Близнецы УРА!')
            print('-' * 108)
        elif 'бу' in slovo:
            if rand in range(0, 34):
                print('Тебя убьют матыгой')
            elif rand in range(34,67):
                print('Ты купишь себе новый трактор')
            elif rand in range(67, 101):
                print('Ты станешь самым грутым на селе')
            print('-' * 108)