def findItem(arr, target):
    for i in arr:
        if i == target:
            return True

    return False


# x = [1,2,4,1]
# target = 5


def binary_search(sortedArray, value):
    n = len(sortedArray)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < sortedArray[middle]:
            right = middle - 1
        elif value > sortedArray[middle]:
            left = middle + 1
        else:
            return middle

    raise ValueError('Value is not in the list')


sortedArray = [2, 5, 3, 4, 1]
binary_search(sortedArray, 7)