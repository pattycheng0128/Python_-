class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, I am %s and %d years old" % (self.name, self.age))


class Student(Teacher):
    def __init__(self, name, age, sid):
        super().__init__(name, age)
        self.sid = sid

    def show_sid(self):
        print("My student ID is %s" % self.sid)

    # override 父類別的 function
    def say_hello(self):
        print("My sid is %s" % self.sid)


if __name__ == "__main__":
    stu = Student("Patty", 18, "S1222")
    stu.say_hello()
    stu.show_sid()
    stu.say_hello()


