pudge = input('Вводите числа (для остановки - off) - ')
list1 = []
list1.append(int(pudge))
count = min(list1)
while pudge != 'off':
    pudge = input()
    if pudge != 'off':
        list1.append(int(pudge))
list2 = []
list2.extend(list1)
list2.sort()
doter = 0
for i in list1:
    if list2 == list1 and i == count:
        count += 1
        doter += 1
if doter == len(list1) and doter != 1:
    print('ok')
else:
    print('net')