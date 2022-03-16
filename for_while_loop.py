# ex1
names = ["Lulu", "Penny", "Joe"]
for name in names:
    print(name)


# ex2
dict = {'a': 1, 'b': 2, 'c': 3}
for key in dict:
    if key == "a":
        print(key)
        break
    else:
        print("error")


# 拆數字
import random

n = random.randint(1, 10)
guess = int(input("請輸入1~10數字:"))

while n != guess:
    if guess < n:
        print("您猜的數字較小")
        guess = int(input("請輸入1~10數字:"))
    elif guess > n:
        print("您猜的數字較大")
        guess = int(input("請輸入1~10數字:"))
print("您猜對了")