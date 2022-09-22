ZINA = int(input('Введите цену - '))
while ZINA != 0:
    Ckidka = int(input('Введите скидку в процентах - '))
    Ckidka = Ckidka / 100
    ZINA = ZINA * Ckidka
    print('Стоимость товара со скидкой =' + str(ZINA))
    ZINA = int(input('Введите цену - '))
print('Cпасибо за покупки')