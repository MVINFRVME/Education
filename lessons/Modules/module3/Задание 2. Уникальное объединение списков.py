# Задание 2. Уникальное объединение списков
# Контекст
# Вы работаете в команде разработки программного обеспечения для компании, которая занимается обработкой и анализом
# данных. Ваша команда получает данные из различных источников, вам нужно объединить их в один отсортированный список
# для дальнейшей обработки. Однако источники данных возвращают отсортированные списки с возможными дубликатами, и ваша
# задача — создать программу, которая объединит эти списки в один отсортированный список без дубликатов.

# Задача
# Напишите программу, которая объединяет два отсортированных списка целых чисел в один отсортированный список
# без дубликатов.

# Пример:

# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 5, 6, 8, 10]
# merged = merge_sorted_lists(list1, list2)
# print(merged)
# Вывод в консоли:

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Советы
# Учтите, что один список может быть короче другого.
# Проверьте ваше решение с различными тестовыми данными, включая случаи с пустыми списками, списками без дубликатов и
# списками с повторяющимися элементами.Требование отсутствия дубликатов значительно усложняет задачу. Убедитесь, что в
# вашем итоговом списке дубликатов не будет.


def merge_sorted_lists(first_list, second_list):
    first_list.extend(second_list)
    first_list.sort()
    index = 1
    while index < len(first_list):
        if first_list[index] == first_list[index - 1]:
            first_list.remove(first_list[index])
        else:
            index += 1
    return first_list


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)
