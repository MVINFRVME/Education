def removeElement(nums, val):
    k = 0
    for x in nums:
        if nums[x] != val:
            nums[k] = nums[x]
            k += 1
    return k


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

print(removeElement(nums, val))
