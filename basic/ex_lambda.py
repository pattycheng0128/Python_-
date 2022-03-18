# 注意: lambda 不能用 block 區塊, 較複雜要用一般的def定義
bmi = lambda w, h: w/h**2
print(bmi(65, 1.5))

# lambda use if..else
res = lambda x:"體重過輕" if x<18.5 else "體重過輕" if x>=24 else "體重過重"
print(res(bmi(60, 1.77)))

# filter 過濾序列
arr = [4, 7, 2, 10, 33, 66]
f = filter(lambda x:x>=10, arr)
print(list(f))

# map 對序列做映射
arr = [1, 4, 7]
m = map(lambda x:x**2, arr)
print(list(m))
