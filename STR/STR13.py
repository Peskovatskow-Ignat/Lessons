list1 = []
string = input()
peremenny = ''
for t in string:
    if t == ' ':
        list1.append(peremenny)
        peremenny = ''
    else:
        peremenny += t
list1.append(peremenny)
for z in list1:
    if '@' in z:
        print(z)
        break