##Выводит большее значение
x = int(input())
y = int(input())

c = (((x - y) //100000000000000000) +1) * x
v = (((y - x) //100000000000000000) +1) * y

print(c + v)