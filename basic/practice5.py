from abc import ABCMeta, abstractmethod


class Employee(metaclass = ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @abstractmethod
    def get_salary(bonus):
        pass


class Manager(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.salary = 45000
    
    
    def get_salary(self, bonus):
        total_amount = self.salary  + bonus
        print("Manager 您的月薪是 %d" % total_amount)


class Teacher(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.salary = 40000
        
    def get_salary(self, bonus):
        total_amount = self.salary + bonus
        print("Teacher 您的月薪是 %d" % total_amount)
    


if __name__ == "__main__":
    Mary = Teacher("Mary", 30)
    Mary.get_salary(2000)
    
    John = Manager("John", 40)
    John.get_salary(3000)

