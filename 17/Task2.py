"""
Создайте класс который будет устанавливать свойство name и иметь метод
который к имени прибавляет надпись "гений". Создайте еще 1 класс, унаследуйте предыдущий.
Во втором классе вызовите метод класса родителя и добавьте к выводу надпись "но его отчислят если он не будет учить ООП".
Создайте экземпляр второго класса с вашим именем и вызовите метод печатающий всю надпись.
"""


class A:
    def __init__(self,name):
        self.name = name

    def print_name(self):
        print(self.name, "гений")


class B(A):
    def print_name(self):
        super().print_name()
        print("но его отчислят если он не будет учить ООП")


Areg = B("Areg")
Areg.print_name()