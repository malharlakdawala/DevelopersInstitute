def mergeSortedArrays(L, R):
    sorted_array = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            sorted_array.append(L[i])
            i += 1
        else:
            sorted_array.append(R[j])
            j += 1

            # When we run out of elements in either L or M,
    # pick up the remaining elements and put in A[p..r]
    while i < len(L):
        sorted_array.append(L[i])
        i += 1

    while j < len(R):
        sorted_array.append(R[j])
        j += 1

    return sorted_array


def mergeSort(nums):
    # exit condition!!! Important for a recursion!
    if (len(nums) <= 1):
        return nums

    # split the array to two smaller arrays
    middle = len(nums) // 2
    L = nums[:middle]
    R = nums[middle:]

    # sort the smalle5r arrays
    L = mergeSort(L)
    R = mergeSort(R)

    nums = mergeSortedArrays(L, R)

    return nums


array = [6, 5, 12, 10, 9, 1]
mergeSort(array)
print(array)