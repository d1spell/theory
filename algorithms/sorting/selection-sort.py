def selection_sort(arr):
    n = len(arr)
    for pos in range(n - 1):
        for i in range(pos + 1, n):
            if arr[i] < arr[pos]:
                tmp = arr[i]
                arr[i] = arr[pos]
                arr[pos] = tmp
    return arr


array = [4, 22, 41, 40, 27, 31, 36, 1, 42, 39, 14, 9, 3, 6, 34, 9, 21, 4, 29, 49]
print(selection_sort(array))
