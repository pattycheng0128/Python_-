class Person:
    # 類別產生實例 instance 時, 初始化的動作
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello %s, I am %s" % (self.name, self.age))

    @staticmethod
    def response_test(yourname):
        print("Hello %s" % (yourname))


per = Person("Patty", 19)
per.say_hello()
Person.response_test("Mary")