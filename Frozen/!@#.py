katikova = 'MCMXCIV'
Slovar = {'I': 1, 'X': 10, 'V': 5, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
COUNT = 0
for i in range(len(katikova) - 1):
    cur = katikova[i]
    next = katikova[i+1]
    if cur == 'I':
        if next == 'V' or next == 'X':
            COUNT -= Slovar[cur]
        else:
            COUNT += Slovar[cur]
    if cur == 'X':
        if next == 'L' or next == 'C':
            COUNT -= Slovar[cur]
        else:
            COUNT += Slovar[cur]
    if cur == 'C':
        if next == 'D' or next == 'M':
            COUNT -= Slovar[cur]
        else:
            COUNT += Slovar[cur]
    else:
        COUNT += Slovar[cur]

COUNT += Slovar[katikova[-1]]

print(COUNT)