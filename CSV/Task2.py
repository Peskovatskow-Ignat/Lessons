"""
Из данных в файле Task1.csv сделайте словарь вида:
(Имя,фамилия):{оценка: звание}
"""

import csv

dict1 = {}

with open("Task1.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    for row in list(reader):
        # dict1 = dict1[row[0], row[1]] = row[2]
        dict1[(row[0], row[1])] = (row[2], row[3])


for i in dict1:
    print(i, dict1[i])