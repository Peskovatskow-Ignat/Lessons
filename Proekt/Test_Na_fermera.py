def test():
    print('------------------------------------------------------------------------------------------------------------')
    count1 = 0
    print('Тест состоит из 7 вопросов')
    naср = input('Ты готов стать фермером(Да/Нет) - ')
    naср = naср.lower()
    if 'да' in naср:
        if naср == 'да':
            print('-' * 108)
            print('Тест начался, выберите правильный вариант ответа!')
            print('-' * 108)
            print('Вопрос 1: Какой самый любимый сезон в деревне?')
            print('1) Лето')
            print('2) Зима')
            print('3) Осень')
            print('4) Весна')
            print('-' * 108)
            otvet = input('Введи номер правильного ответа - ')
            if otvet == '2':
                count1 +=1
            print('-' * 108)
            print('Вопрос 2: Как обычно называют корову?')
            print('1) Бурёнка')
            print('2) Саня')
            print('3) Анютка')
            print('4) "Эй сюда иди"')
            print('-' * 108)
            otvet = input('Введи номер правильного ответа - ')
            if otvet == '1':
                count1 +=1
            print('-' * 108)
            print('Вопрос 3: Любит ли свинка когда ей чешут пузико?')
            print('1) Нет')
            print('2) Какого чёрта я извиняюсь')
            print('3) Я на колхозника похож?')
            print('4) Кайфует как Dava')
            print('-' * 108)
            otvet = input('Введи номер правильного ответа - ')
            if otvet == '4':
                count1 +=1
            print('-' * 108)
            print('Вопрос 4: Что такое гектар?')
            print('1) Модель телефона')
            print('2) Шоколадка')
            print('3) Матное слово')
            print('4) Каждый день вспахиваю 10 гектаров земли')
            print('-' * 108)
            otvet = input('Введи номер правильного ответа - ')
            if otvet == '4':
                count1 +=1
            print('-' * 108)
            print('Вопрос 5: Со скольки лет можно ездить на машине?')
            print('1) С 18 лет')
            print('2) С 21 года')
            print('3) Главное чтобы товарищи полицаи не спалили')
            print('4) с 14 лет')
            print('-' * 108)
            otvet = input('Введи номер правильного ответа - ')
            if otvet == '3':
                count1 +=1
            print('-' * 108)
            print('Вопрос 6: Во что играют в колхозе?')
            print('1) CS GO')
            print('2) Во что им вздумается')
            print('3) Dota 2')
            print('4) Babl Kvas')
            print('-' * 108)
            otvet = input('Введи номер правильного ответа - ')
            if otvet == '2':
                count1 +=1
            print('-' * 108)
            print('Вопрос 7: Когда ты считаешь овец?')
            print('1) Считаю овец когда ложусь спать')
            print('2) Что это значит?')
            print('3) Каждые 5 минут')
            print('4) С утра чтобы матушке доложить')
            print('-' * 108)
            otvet = input('Введи номер правильного ответа - ')
            if otvet == '1':
               count1 +=1
            print('-' * 108)
            print('Итог:')
            print('-' * 108)
            if count1 in range(0,3):
                print('Чувак ты из города тебе тут не место')
            elif count1 in range(3, 5):
                 print('Ну в колхозе бы тебя не приняли за своего')
            else:
                print('Чувак ты реально всю жизнь прожил в колхозе??? Красавчик')
            print('-' * 108)
    else:
        print('Уходи отсюда Городской')
