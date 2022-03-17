class Car:
    def __init__(self, color, kilometer):
        self.color = color
        self.kilometer = kilometer

    def your_color(self):
        print("您輸入的顏色:", self.color)

    def go_ahead(self):
        print("車子正在已%d速度前進" % self.kilometer)


if __name__ == "__main__":
    test = Car("red", 20)
    test.your_color()
    test.go_ahead()