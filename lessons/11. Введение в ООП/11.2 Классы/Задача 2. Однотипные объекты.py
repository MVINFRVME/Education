# Задача 2. Однотипные объекты
# В офис заказали небольшую партию из четырёх мониторов и трёх наушников. У монитора есть четыре характеристики:
# название производителя, матрица, разрешение и частота обновления экрана. Все четыре монитора отличаются только
# частотой.

# У наушников три характеристики: название производителя, чувствительность и наличие микрофона. Отличие только в наличии
# микрофона.

# Для внесения в базу программист начал писать такой код:
# monitor_name_1 = 'Samsung'
# monitor_matrix_1 = 'VA'
# monitor_res_1 = 'WQHD'
# monitor_freq_1 = 60
# monitor_name_2 = 'Samsung'
# monitor_matrix_2 = 'VA'
# monitor_res_2 = 'WQHD'
# monitor_freq_2 = 144
# monitor_name_3 = 'Samsung'
# monitor_matrix_3 = 'VA'
# monitor_res_3 = 'WQHD'
# monitor_freq_3 = 70
# monitor_name_4 = 'Samsung'
# monitor_matrix_4 = 'VA'
# monitor_res_4 = 'WQHD'
# monitor_freq_4 = 60

# headphones_name_1 = 'Sony'
# headphones_sensitivity_1 = 108
# headphones_micro_1 = False
# headphones_name_2 = 'Sony'
# headphones_sensitivity_2 = 108
# headphones_micro_2 = True
# headphones_name_3 = 'Sony'
# headphones_sensitivity_3 = 108
# headphones_micro_3 = True

# Поправьте программиста: перепишите код, используя классы и экземпляры классов.

# class Monitor:
#     name = 'Samsung'
#     matrix = 'VA'
#     res = 'WQHD'
#     freq = 60

# class Headphones:
#     name = 'Sony'
#     sensetivity = 108
#     micro = False

# monitor_1, monitor_2, monitor_3, monitor_4= Monitor(), Monitor(), Monitor(), Monitor()
# headphones_1, headphones_2, headphones_3 = Headphones(), Headphones(), Headphones()

# monitor_2.freq = 144
# monitor_3.freq = 70
# monitor_4.freq = 60

# headphones_2.micro = True
# headphones_3.micro = True

class Monitor:
    name = "Samsung"
    matrix = "VA"
    resolution = "WQHD"
    frequency = 0


class Headphones:
    name = "Sony"
    sensitivity = 108
    micro = True


monitors = [Monitor() for _ in range(4)]
headphones = [Headphones() for _ in range(3)]

for index, number in enumerate([60, 144, 70, 60]):
    monitors[index].frequency = number

headphones[0].micro = False
