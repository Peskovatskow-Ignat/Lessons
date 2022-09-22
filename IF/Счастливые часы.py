Time = int(input('Время - '))
summa = int(input('Цена - '))
if Time in range(10, 13):
    summa = summa/2
    print(summa)
elif Time in range(20, 23):
    summa = summa/4
    print(summa)
elif Time in range(8,10) or Time in range(13, 20): #Прекол
    print(summa)
else:
    print('Магазин закрыт')