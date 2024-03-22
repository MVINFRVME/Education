people_amt = int(input('Кол-во участников: '))
team_amt = int(input('Кол-во человек в команде: '))
list_of_members = []
num = 1

if people_amt % team_amt == 0:
    for _ in range((people_amt // team_amt), ):
        list_of_members.append(list(range(num, num + 3)))
        num += 3
    print(f'Общий список команд: {list_of_members}')

else:
    print(f'{people_amt} участников невозможно поделить на команды по {team_amt}')

# Вариант учителя
# human_count = int(input("Кол-во участников: "))
# team_count = int(input("Кол-во человек в команде: "))
# if human_count % team_count == 0:
#     teams = []
#     teammate_number = 0
#     for _ in range(human_count // team_count):
#         new_team = []
#         for _ in range(team_count):
#             teammate_number += 1
#             new_team.append(teammate_number)
#         teams.append(new_team)
#     print(teams)
# else:
#     print(human_count, "невозможно поделить на команды по", team_count, "человек!")