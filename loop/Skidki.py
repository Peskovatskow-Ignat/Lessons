Zina = int(input('Цена товара - '))
count1 = 0
while Zina % 2 == 0:
    Zina = Zina / 2
    count1 += 1
if count1 > 0:
    print('К оплате -', Zina)
else:
    print('К оплате -', Zina * 0.75)
print('Спасибо Спасибоооооооооо')

