list1 = [3, 5, 1, 9]
print(list1[:2])
print(list1[-1])

# extend 增加多個元素
list2 = [6, 7]
list1.extend(list2)
print(list1)


# append 增加2個以上的元素會是list中的list, 通常是增加1個
list3 = [3, 2]
list1.append(list3)
print(list1)

# remove 刪除元素
list1.remove(5)
print(list1)
# pop 刪除 index(沒寫是刪除最後一個index)
list1.pop()
print(list1)

# sort 排序
arr = [2, 6, 1, 4, 0]
arr.sort()
print(arr)

# reverse() 反序
arr.reverse()
print(arr)

# tuple
t = (4, 3, 9)
print(4 in t)
print(0 in t)

# len()
print("計算長度:", len(t))
# count() 確認某個數字或字串出現幾次
arr = [4, 2, 9, 2, 0]
print("出現過幾次:", arr.count(0))
greeting = "hello,pp"
print("出現過幾次:", greeting.count("p"))
