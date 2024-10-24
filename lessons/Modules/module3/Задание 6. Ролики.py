# Задание 6. Ролики
# Что нужно сделать
# Частная контора даёт в прокат ролики самых разных размеров. Человек может надеть ролики только своего размера.
# Пользователь вводит два списка размеров: N размеров роликов и K размеров ног людей. Реализуйте код, который
# определяет, какое наибольшее число человек может одновременно взять ролики и пойти кататься.
#
# Пример:
#
# Количество роликов: 4
#
# Размер пары 1: 41
#
# Размер пары 2: 40
#
# Размер пары 3: 39
#
# Размер пары 4: 42
#
#
# Количество людей: 3
#
# Размер ноги человека 1: 42
#
# Размер ноги человека 2: 41
#
# Размер ноги человека 3: 42
#
# Наибольшее количество людей, которые могут взять ролики: 2
#
# Советы и рекомендации
# Помните, по условиям задачи размер роликов должен быть равен размеру ноги. Чтобы подобрать максимальное количество
# пар, старайтесь найти наименьший возможный размер роликов для каждого размера ноги.

rollers_list = []
rollers_amt = int(input("Количество роликов: "))
for i in range(rollers_amt):
    roller_size = int(input(f"Размер пары {i + 1}: "))
    rollers_list.append(roller_size)
rollers_list.sort()


foots_list = []
people_amt = int(input("Количество людей: "))
for i in range(people_amt):
    foot_size = int(input(f"Размер ноги человека {i + 1}: "))
    foots_list.append(foot_size)
foots_list.sort()

total_matches = 0
matches = 0

while True:
    for roller in rollers_list:
        for foot in foots_list:
            if foot == roller:
                foots_list.remove(foot)
                rollers_list.remove(roller)
                matches += 1
    total_matches += matches
    if total_matches - matches == total_matches:
        break
    matches = 0

print(f"Наибольшее количество людей, которые могут взять ролики: {total_matches}")
