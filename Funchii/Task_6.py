"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""
list1 = []


def main():
    pisem()
    Proverka()



def pisem():
    for x in range(3):
        x = input()
        list1.append(x)


def Proverka():
    for i in list1:
        if i != 'None':
            print(i)


main()