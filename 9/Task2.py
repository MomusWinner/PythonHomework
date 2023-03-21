"""
Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси.
"""


def calculation_of_money(distance):
    if distance >= 140:
        distance -= 140
        return calculation_of_money(distance) + 0.25
    else:
        return 4

print(calculation_of_money(100))