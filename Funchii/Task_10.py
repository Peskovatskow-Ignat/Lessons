"""
Очень часто веб-дизайнеры используют HEX-значение какого-либо цвета.
Напишите программу принимающую 2 позиционных аргумента: слово "Цвета" и количество цветов.
и произвольное количество значений Цвет : HEX. Программа должна вывести все данные на экран.
"""

def hex_to_rjb( colour):
    colour = colour.lstrip('#')
    lv = len(colour)
    return tuple(int(colour[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))



first = input("Ввидите цвета или Q: ")
ans = []
while True:
    if first == 'Q':
        break
    elif first == "цвета":
        hex = input("Введите hex цвета: ")
        rgb = hex_to_rjb(hex)
        print("Ваш цвет", rgb)
    else:
        print("Нет такой команды")

    first = input("Ввидите цвета или Q: ")


