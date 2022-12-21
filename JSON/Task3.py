"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: [
{
name:***
time:***
cities:***
}
]
"""

import json
import pprint
from datetime import datetime


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%D")


task = ["oleg", 24, ["Belarus", "Russia"], (24, 1), ["Moscow", "Vladikavkaz", 'Krasnodar', "Rostov", "Nalchik"]]
countris = [{"name": task[2], "date": current_date, "time": current_time, "cities": task[4]}]
dict1 = {"Name": task[0], "Age": task[1], "Countries": countris}

with open("Pesk_ignat_3.json", "w") as Oleg:
    json.dump(dict1, Oleg, indent=4)

with open("Pesk_ignat_3.json", "r") as info:
    data = json.load(info)

pprint.pprint(data)
