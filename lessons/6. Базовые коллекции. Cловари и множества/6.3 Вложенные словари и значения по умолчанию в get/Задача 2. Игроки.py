# Задача 2. Игроки
# Есть готовый словарь игроков, у каждого игрока есть имя, команда, в которой он играет, а также его текущий статус,
# в котором указано, отдыхает он, тренируется или путешествует:

players_dict = {
    1: {"name": "Vanya", "team": "A", "status": "Rest"},
    2: {"name": "Lena", "team": "B", "status": "Training"},
    3: {"name": "Maxim", "team": "C", "status": "Travel"},
    4: {"name": "Egor", "team": "C", "status": "Rest"},
    5: {"name": "Andrei", "team": "A", "status": "Training"},
    6: {"name": "Sasha", "team": "A", "status": "Rest"},
    7: {"name": "Alina", "team": "B", "status": "Rest"},
    8: {"name": "Masha", "team": "C", "status": "Travel"},
}

# Напишите программу, которая выводит на экран следующие данные в разных строках:
# Все члены команды А, которые отдыхают.
# Все члены команды B, которые тренируются.
# Все члены команды C, которые путешествуют.

print("Все члены команды А, которые отдыхают: ", end="")
for i_num in players_dict.values():
    if i_num["team"] == "A" and i_num["status"] == "Rest":
        print(i_num["name"], end=" ")

print("\nВсе члены команды B, которые тренируются: ", end="")
for i_num in players_dict.values():
    if i_num["team"] == "B" and i_num["status"] == "Training":
        print(i_num["name"], end=" ")

print("\nВсе члены команды C, которые путешествуют: ", end="")
for i_num in players_dict.values():
    if i_num["team"] == "C" and i_num["status"] == "Travel":
        print(i_num["name"], end=" ")

# или через list_comprehension
#
# team_a_members = [player['name']
#     for player in players_dict.values()
#     if player['team'] == 'A' and player['status'] == 'Rest'
# ]
# print(team_a_members)
