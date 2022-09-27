count = 0
count1 = 0
dlina = []
otenki = input('Введите оценки - ')
otenki.split(' ')
for i in otenki:
    if i == '5':
        count1 +=1
        dlina.append(i)
    else:
        count +=1
        dlina.append(i)
itogo = (count1 / count) * 100
print('Количество пятёрок -', count1)
print('Средний балл получения пятёрок -', itogo)

