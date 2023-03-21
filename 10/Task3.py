"""
На летней универсиаде будет проводиться по два забега. Чтобы соревнования были честными,
участники должны распределяться между забегами случайным образом.
Напишите программу, печатающую случайные номера забегов (1 или 2) до тех пор, пока не будет введено «off».
После генерации каждого номера должно печататься:
1) «Ваш номер: _».
2) «Участников в первом забеге: _», «Участников во втором забеге: _».
"""
from random import *

valid = input("Введите off, если хотите закончить: ")
race = {1: 0, 2: 0}


while valid != 'off':
    number_race = randint(1,2)
    print(f"Забег №{number_race}")
    number = randint(1,1000)
    race[number_race] += 1
    print(f"Ваш номер {number}")
    print(f"Участников в первом забеге:{race[1]}. Участников во втором забеге: {race[2]}")
    valid = input("Введите off, если хотите закончить: ")


