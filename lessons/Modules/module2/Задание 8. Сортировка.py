# Задание 8. Сортировка
# Что нужно сделать
# Дан список из N чисел. Напишите программу, которая сортирует элементы списка по возрастанию и выводит их на экран.
# Дополнительный список использовать нельзя.
#
# Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.
#
# Пример:
#
# Изначальный список: [1, 4, –3, 0, 10]
#
# Отсортированный список: [–3, 0, 1, 4, 10]


def selection_sort(my_list):
    for i_mn in range(len(my_list)):
        for curr in range(i_mn, len(my_list)):
            if my_list[curr] < my_list[i_mn]:
                my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]


nums = [1, 4, -3, 0, 10]
print(f"Изначальный список: {nums}")
selection_sort(nums)
print(f"Отсортированный список: {nums}")
