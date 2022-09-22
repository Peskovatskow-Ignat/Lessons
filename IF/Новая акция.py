Tovar1 = int(input('Товар 1 - '))
Tovar2 = int(input('Товар 2 - '))
Tovar3 = int(input('Товар 3 - '))
Dengi = 0
if Tovar1 < Tovar2 < Tovar3:
    Dengi = (Tovar1 + Tovar2 +Tovar3)/2
    print('Акция - ', Dengi)
elif Tovar1 > Tovar2 > Tovar3:
    Dengi = (Tovar1 + Tovar2 + Tovar3) / 3
    print('Акция - ', Dengi)
else:
    Dengi = (Tovar1 + Tovar2 + Tovar3)
    print('К оплате - ', Dengi)