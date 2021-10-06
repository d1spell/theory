
def binary_search(lst: List, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high)
        guess = lst[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
