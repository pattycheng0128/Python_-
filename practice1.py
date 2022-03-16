# ex: 1英吋 = 2.54公分

length = float(input("請輸入長度:"))
unit = input("請輸入轉換的單位(in/cm):")

if unit == "in":
    print(length)
    print("%f in = %f cm" % (length, length * 2.54))
elif unit == "cm":
    print(length)
    print("%f cm =  %f in" % (length, length/2.54))
else:
    print("輸入錯誤")


