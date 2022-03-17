# def single_number(nums):
#     # 2 * (a+b+c) - (2a+2b+c)
#     return 2 * sum(set(nums)) - sum(nums)
#
#
# print(single_number([1, 3, 3]))

# two sum
def two_sum(nums, target):
    # 空字典
    hashmap = {}

    # 外面 loop 要跑幾次
    for i in range(len(nums)):
        # 目標值 = target - nums 裡面的值
        current = target - nums[i]
        # 確認 current 是否在 hashmap字典內
        if current in hashmap:
            return[i, hashmap[current]]
        # 不在 hashmap字典內, 就加到字典內(key是array的數值, i 是 index)
        hashmap[nums[i]] = i


print(two_sum([2, 7, 11, 15], 9))
# print(two_sum([3,2,4], 6))
# print(two_sum([3, 3], 6))

