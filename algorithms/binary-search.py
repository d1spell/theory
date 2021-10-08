def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


array = [1, 3, 4, 4, 6, 9, 9, 14, 21, 22, 27, 29, 31, 34, 36, 39, 40, 41, 42, 49]

print(binary_search(array, 39))
