my_list = [1, 2, 3, 4, 5]
my_list.insert(0, my_list.pop(-1))  # Циклический сдвиг вправо на одну позицию
print(my_list)
#
# my_list = [1, 2, 3, 4, 5, 6]
# shift = len(my_list) - 1
# rotated_list = my_list[shift:] + my_list[:shift]
# print(rotated_list)
