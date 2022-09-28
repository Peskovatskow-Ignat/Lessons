"""
Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
а в качестве значения количество этих цифр в строке
"""
numbers = "0139412831055230677798"
count = 0
Slovar = {}
for i in range(10):
    Slovar[i] = numbers.count(str(i))
Chelovek = int(input())
print(Slovar[Chelovek])