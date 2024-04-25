dist = 15.0  # начинаем с дистанции 15 км
weekly_increase = dist / 100 * 7.5  # 7.5% увеличение дистанции в неделю (рекомендуется увеличение объема до 10% в нед.)
weeks = 12  # недель до марафона

for week in range(weeks):
    weekly_increase = dist / 100 * 7.5
    dist += weekly_increase
    print(f'{week + 1} неделя: {round(dist, 2)}')

#
#
# print(f'Максимальная дистанция {round(dist, 2)}')
# # Максимальная дистанция 35.73
