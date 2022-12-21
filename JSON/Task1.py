"""
Выведите из файла character.json Имя персонажа,родную планету и список эпизодов в которых он появлялся.
"""

import json

with open("character.json", "r") as dead:
    data = json.load(dead)


name = data["name"]
planet = data["origin"]["name"]


def info(name, planet):
    print(
        f"Имя персонажа - {name}. Он покинул свою родную планету {planet} \nОн побывал во многих эпизодах таких как:"
         )
    for i in data["episode"]:
        print(f"-{i}")


info(name, planet)
