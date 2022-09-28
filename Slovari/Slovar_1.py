"""
Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
"""
Zadanie = {}
for i in range(1, 11):
    Zadanie[i] = i * i *i
n = int(input())
print(Zadanie[n])