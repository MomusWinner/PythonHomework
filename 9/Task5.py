"""
Очень часто веб-дизайнеры используют HEX-значение какого-либо цвета.
Напишите программу принимающую 2 позиционных аргумента: слово "Цвета" и количество цветов.
и произвольное количество значений Цвет : HEX. Программа должна вывести все данные на экран.
"""


def info_hex(colors: str, color_number: int, **hex_colors):
    return f"{colors} количество: {color_number}\n {hex_colors}"

print(info_hex("Цвет",5, white="#fffff",black="#00000"))