import random

from timer import timer


def randomArray(n):
    nums = [random.randint(1, n * 100) for i in range(n)]
    return nums


@timer
def brute_subsetsum(numbers, target):
    for i in numbers:
        for n in numbers:
            if i + n == target:
                print(f"{i} + {n} = {target}")
                return True

    print(f"target {target} was not founded in array ")
    return False

# nums = randomArray(100)
# brute_subsetsum(nums,1)
# nums = randomArray(1000)
# brute_subsetsum(nums,2)
# nums = randomArray(10000)
# brute_subsetsum(nums,3)

