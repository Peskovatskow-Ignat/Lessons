"""
Создайте список предметов формата Название, препод, ваша любовь к предмету(от 0 до 10).
Сохраните в CSV файл(название файла - ваша фамилия).
P.S не менее 4 столбцов.
"""

import csv
import pprint

spisok = [["Название_Предмета", "Преподаватель", "Любовь"],
          ["Англиский", "Бикинина", "3"],
          ["ПИТОНЧИК", "Олеженька", "10"],
          ["Сети", "Головин", "8"],
          ["Базы_данных", "Голоднюк", "6"]]

with open("Pesk_Ignat.csv", "w+") as f:
    writer = csv.writer(f, delimiter=";")
    for i in spisok:
        writer.writerow(i)

    f.seek(0)

    riader = csv.reader(f)
    for row in list(riader):
        print(row)

