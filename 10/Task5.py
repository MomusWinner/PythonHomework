"""
Напишите программу-имитатор подбрасывания 2 кубиков.
Программа выводит на экран "подбрасываю кубики" и спустя 2 секунды выводит значения на кубиках в одну строку.
"""
from random import randint
from time import sleep

string = input("Подбросить кубики(да(введите что угодно)/нет): ").lower()
while string != "нет":
    print("подбрасываю кубики")
    sleep(2)
    print(f"{randint(1,6)}{randint(0,6)}")
    string = input("Подбросить кубики(да(введите что угодно)/нет): ").lower()