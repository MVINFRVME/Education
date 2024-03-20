# Задание 3. Видеокарты
# Что нужно сделать
# В базе магазина электроники есть список видеокарт компании NVIDIA разных поколений.
# Вместо полных названий хранятся только числа, которые обозначают модель и поколение видеокарты.
# Недавно компания выпустила новую линейку видеокарт. Самые старшие поколения разобрали за пару дней.
# Напишите программу, которая удаляет наибольшие элементы из списка видеокарт.

# Пример:

# Количество видеокарт: 5

# Видеокарта 1: 3070

# Видеокарта 2: 2060

# Видеокарта 3: 3090

# Видеокарта 4: 3070

# Видеокарта 5: 3090

# Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]

# Новый список видеокарт: [ 3070 2060 3070 ]

ammount = int(input('Введите количество видеокарт: '))

GPU_list = []
GPU_max = 0

for i in range(ammount):
    GPU = int(input(f'Видеокарта {i + 1}: '))
    GPU_list.append(GPU)
    if GPU_max < GPU:
        GPU_max = GPU

print(f'Старый список видеокарт: {GPU_list}')

new_GPU_list = []
for GPU in GPU_list:
    if GPU_max != GPU:
        new_GPU_list.append(GPU)

print(f'Новый список видеокарт: {new_GPU_list}')