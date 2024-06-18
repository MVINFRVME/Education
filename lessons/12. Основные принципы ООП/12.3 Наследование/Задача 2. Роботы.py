# Задача 2. Роботы
# На военную базу завезли несколько интересных моделей роботов, которые похожи между собой, но имеют немного разные
# функции. У каждого робота есть номер модели и действие operate, которое означает, что делает робот. Особенности
# роботов следующие:

# У робота-пылесоса есть мешок для мусора, изначально он пустой (0). При команде operate робот сообщает, что он
# пылесосит пол, и выводит текущую заполняемость мешка.

# У военного робота есть оружие, и при команде operate он выводит сообщение о защите военного объекта с помощью этого
# оружия.

# Ещё есть робот — подводная лодка, который также является военным. У этого робота есть значение глубины, и при команде
# operate он делает то же, что и военный робот, плюс сообщает, что охрана ведётся под водой.

# Напишите программу, которая реализует все необходимые классы роботов.

class Robot:
    def __init__(self, serial_number):
        self.serial_number = serial_number

    def __str__(self):
        return f'{self.__class__.__name__} номер: {self.serial_number}'

    def operate(self):
        print('Робот ездит по кругу.')


class VacuumCleanerRobot(Robot):
    def __init__(self, serial_number):
        super().__init__(serial_number)
        self.bag = 0

    def operate(self):
        print('Пылесосим...')
        self.bag += 1
        print('В мешке {garbage} ед. мусора.'.format(garbage=self.bag))


class CombatRobot(Robot):
    def __init__(self, serial_number, weapon):
        super().__init__(serial_number)
        self.weapon = weapon

    def operate(self):
        print('Защищаем военный объект с помощью {item}.'.format(item=self.weapon))


class SubmarineRobot(CombatRobot):
    def __init__(self, serial_number, weapon, depth):
        super().__init__(serial_number, weapon)
        self.depth = depth

    def operate(self):
        super().operate()
        print('Охрана ведется на глубине {value} м.'.format(value=self.depth))


pilesos = VacuumCleanerRobot(282)
print(pilesos)
pilesos.operate()
print()

warrior = CombatRobot(123, 'AK-47')
print(warrior)
warrior.operate()
print()

water_bratok = SubmarineRobot(748, 'Гарпун', 659)
print(water_bratok)
water_bratok.operate()
