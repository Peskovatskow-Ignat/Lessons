"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: ***
"""
import json
import pprint

task = ["oleg", 24, ["Belarus", "Russia"]]
dict = {"Name": task[0], "Age": task[1], "Countries": task[2][0]}

with open("Pesk_ignat_2.json", "w") as Oleg:
    json.dump(dict, Oleg, indent=4)

with open("Pesk_ignat_2.json", "r") as print_info:
    info = json.load(print_info)

pprint.pprint(info, indent=4)
