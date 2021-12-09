import random


def subsetsum(arr, num):
    flag = 0

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if num == arr[i] + arr[j]:
                print("the numbers are ", arr[i], arr[j])
                flag = 1
                break

    print("no numbers found") if flag == 0 else None


def subset_dict(nums, num):
    new_dict = dict(zip(nums, nums))
    flag = 0
    for key in new_dict.keys():
        num_chk = num - key
        if num_chk in new_dict.keys():
            print("the numbers are", num_chk, key)
            flag = 1
            break
    print("no numbers found") if flag == 0 else None

nums = [12, -7, 20, 1, 4, -10, -1]
subset_dict(nums, 3)

# subsetsum(nums, 4)

nums_dict = {12: True, -7: True, 20: True, 1: True, 4: True, -10: True, -1: True}
# print(nums_dict[12])

#### Suggested Method
# def subsetsum(numbers, target):
#     checkedNumbers = {}
#     for num in numbers:
#         if (target - num) in checkedNumbers:  # 1 action :)
#             print(f"True {num} + {(target - num)} = {target}")
#             return True
#         else:
#             checkedNumbers[num] = True
#
#     print(f"False {target}")
#     return False
#
#
# numbers = [3, 8, 6, -1, -4, 10]
# subsetsum(numbers, 5)
# subsetsum(numbers, 89)
# subsetsum(numbers, 1)
# subsetsum(numbers, 11)