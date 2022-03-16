# 字典
dict1 = {'a': 1, 'b': 2, 'c': 3}
# print(dict1["d"])
# 如果 key 沒在字典內, 會印出 no data
print(dict1.get("d", "no data"))

# 使用 tuple 當 key
dict2 = {(2, 3): 'A', (5, -3): 'B', (-1, -5): 'C'}
print(dict2[(-1, -5)])

# keys()
print(dict2.keys())

# values()
print(dict2.values())

# items()
print(dict2.items())

# 有找到 key 會修改值, 沒找到 key 會新增內容
dict1["c"] = 4
print(dict1)

# del 刪除
del dict1["c"]
print(dict1)

# clear 清空字典的內容
dict1.clear()
print(dict1)
