def binary_search(seq, item):
    low = 0
    high = len(seq) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = seq[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


nums = [0, 3, 9, 12, 13, 16, 17, 18, 20, 22, 24, 27, 29, 30]
i = 10
print(binary_search(nums, i))
