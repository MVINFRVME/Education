# Задача 1. Свой for (ну почти)
# Дан любой итерируемый объект, например список из N чисел. Реализуйте функцию, которая эмулирует работу цикла for с
# помощью цикла while и проходит во всем элементам итерируемого объекта. Не забудьте про исключение «конца итерации».

nums = [1, 2, 3, 4, 5]

# iterator = nums.__iter__()
# while True:
#     try:
#         print(iterator.__next__())
#     except StopIteration:
#         break

# или
iterator = iter(nums)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        print('The end!')
        break
