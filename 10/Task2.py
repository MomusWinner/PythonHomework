"""
В каждом заплыве участвуют два случайных спортсмена из разных сборных. Напиши программу для печати номеров спортсменов.

1) Программа должна запрашивать количество спортсменов в каждой сборной с сообщением: «Число участников сборной _:».
2) Затем должна печататься пара случайных спортсменов из разных сборных для заплыва в формате: «Пловец _ - пловец _».
"""
from random import randint

national_team1 = int(input())
national_team2 = int(input())

print(f"Пловец {randint(1, national_team1)}")
print(f"Пловец {randint(1, national_team2)}")


