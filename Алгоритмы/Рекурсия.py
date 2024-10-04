# Написать код для ф-ции sum
def summ(nums):
    if nums == []:
        return 0
    return nums[0] + summ(nums[1:])

print(summ([1, 2, 3, 4, 5]))

# Напишите рекурсивную функцию для подсчета элементов в списке.
def count(nums):
    if nums == []:
        return 0
    return 1 + count(nums[1:])


print(count([1, 2, 3, 4, 5]))


# Найти наибольшее число в списке.
def maxi(nums):
    if len(nums) == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    sub_max = maxi(nums[1:])
    return nums[0] if nums[0] > sub_max else sub_max


print(maxi([1, 2, 3, 4, 5]))
