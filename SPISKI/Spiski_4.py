Kolichestvo_ludei = int(input('Количество сотрудников - '))
spisok = []
pipl = []
for i in range(Kolichestvo_ludei):
    infa = input('Введите ФИО - ')
    mesto = input('Должность - ')
    deti = input('Количество детей в группах - ')
    deti.split(',')
    pipl.append(infa)
    pipl.append(mesto)
    pipl.append(deti)
    spisok.append(pipl)
    pipl = []
print(spisok)