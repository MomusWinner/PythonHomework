"""
Пользователь вводит логин. Программа должна проверить все ли символы являются строчными. Если нет, выбросить ошибку.
Если ошибки не произошло писать фразу "Логин добавлен в базу". В не зависимости от того была ли ошибка должно печататься
"Я выучил исключения"
"""

login = input()

try:
    for i in login:
        if not i.islower():
            raise ValueError( "Только строчные")
    print("Логин добавлен в базу")
except ValueError as e:
    print(e)
finally:
    print("Я выучил исключения")