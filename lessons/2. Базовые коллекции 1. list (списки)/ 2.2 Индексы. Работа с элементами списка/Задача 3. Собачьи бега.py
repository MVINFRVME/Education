score_list = []

number_of_dogs = int(input("Введите кол-во собак: "))

for i in range(number_of_dogs):
    score = int(input(f"Введите кол-во очков {i + 1} собаки: "))
    score_list.append(score)

max_score = score_list[0]
min_score = score_list[0]

for score in score_list:
    if score > max_score:
        max_score = score
    if score < min_score:
        min_score = score

new_score_list = []

for num in score_list:
    if num == min_score:
        new_score_list.append(max_score)
    elif num == max_score:
        new_score_list.append(min_score)
    else:
        new_score_list.append(num)

print(score_list)
print(new_score_list)

# ИЛИ
# score_list = []
#
# number_of_dogs = int(input('Введите кол-во собак: '))
#
# for i in range(number_of_dogs):
#     score = int(input(f'Введите кол-во очков {i + 1} собаки: '))
#     score_list.append(score)
#
# max_score = score_list[0]
# min_score = score_list[0]
#
# index = 0
# min_index = 0
# max_index = 0
#
#
# for score in score_list:
#     if score > max_score:
#         max_score = score
#         max_index = index
#     if score < min_score:
#         min_score = score
#         min_index = index
#     index += 1
#
# print(score_list)
# score_list[max_index], score_list[min_index] = score_list[min_index], score_list[max_index]
# print(score_list)
