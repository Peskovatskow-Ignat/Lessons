while True:
    LOG = input('Введите логин - ')
    Zapret = '=?*^$№@_ '
    n = 0
    for i in LOG:
        if i in Zapret:
            print('Недопустимый Сивол', i)
            break
        else:
            n+=1
    if n == len(LOG):
        print('Всё хорошо')
        break