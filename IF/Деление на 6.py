Num = input('Введите число - ')
count = 0
for t in Num:
    count = count + int(t)
if int(Num) % 2 == 0 and count % 3 == 0:
    print(Num, '- Делется на 6')
else:
    print(Num, 'Не делится на 6')
