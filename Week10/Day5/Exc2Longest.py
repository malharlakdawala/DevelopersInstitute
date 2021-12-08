def longest_sequence(arr):
    arr = sorted(arr)
    flag = 0
    flag_store = []
    for i in range(len(arr) - 1):
        if arr[i + 1] == arr[i] + 1:
            flag += 1
        else:
            flag_store.append(flag)
            flag = 0
        flag_store.append(flag)
    print(max(flag_store))
input_array = [6, 206, 4, 205, 100, 207, 5, 200, 208, 3, 201, 202, 203, 204]
longest_sequence(input_array)
