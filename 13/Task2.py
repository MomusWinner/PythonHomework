"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""

with open("areg.txt","r") as fr:
    with open("file.txt","w+") as fw:
        fw.write("но у меня не получается")
        fw.seek(0)
        print(fr.readline(), fw.readline())