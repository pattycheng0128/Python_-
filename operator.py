# BMI 公式: w/h**2
weight = input("請輸入您的體重:")
w = float(weight)
height = input("請輸入您的身高:")
h = float(height)
BMI = w/((h/100)**2)

if BMI < 18:
    print("您體重過輕")
elif BMI >= 18 or BMI < 24:
    print("您體重正常")
elif BMI >= 24 or BMI <= 27:
    print("您體重過重")
else:
    print("您輸入錯誤")

