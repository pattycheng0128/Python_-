# 抽象類別
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 抽象類別好處是可以讓父類別先不用實作, 交由子類別實作就好
    @abstractmethod
    def show_id(self):
        pass


class Teacher(Employee):
    def __init__(self, name, age, tid):
        super().__init__(name, age)
        self.tid = tid

    def show_id(self):
        print("My teacher ID is %s" % self.tid)


tea = Teacher("Penny", 32, "T33222")
tea.show_id()
