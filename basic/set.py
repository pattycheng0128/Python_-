# 集合 set: 集合中的元素不能重複, 也沒有順序性, 無法使用索引值取值
V = {"a", "e", "t", "c"}
F = {"d", "e", "b", "s"}

# 聯集, 兩個元素相加, 但元素不能重複 |
print(V | F)

# 交集, 會抓取相同元素的內容 &
print(V & F)

# 差集, 將兩個元素做減法的動作 -
print(V - F)
print(F - V)

# 反交集, 排除相同的元素 ^
print(V ^ F)

# add 只能新增一個元素
V.add("h")
print(V)

# update 可以新增多個元素
V.update({5, 9, "f"})
print(V)

# remove(), 刪除元素不在裡面會拋出錯誤
V.remove('a')
print(V)

# discard 不會拋出錯誤
V.discard('l')
print(V)

# 判斷是否在 set 裡面
print("e" in V)


