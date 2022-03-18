# python 不支援 overload
def add(a, b):
    return a + b


print(add(4, 9))


# 輸入多個 tuple
def foo(*tmp):
    return tmp


print(foo(3, 9, 3))
