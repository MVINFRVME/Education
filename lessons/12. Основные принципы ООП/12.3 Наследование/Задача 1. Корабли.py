# Задача 1. Корабли
# Даны два класса кораблей — грузовой и военный. У каждого из этих кораблей есть своя модель, и каждый может сделать
# два действия: сообщить свою модель и идти по воде.

# Грузовой корабль имеет такой атрибут, как заполненность, изначально он равен нулю. У него есть ещё два действия:
# погрузить и выгрузить груз с корабля.

# У военного же корабля нет никаких грузов, есть только оружие, которое передаётся вместе с моделью. Также, вместо
# погрузки и выгрузки, у него есть другое действие — атаковать.

# Реализуйте классы грузового и военного кораблей. Для этого выделите общие атрибуты и методы в отдельный класс
# «Корабль» и используйте наследование. Не забудьте про функцию super в дочерних классах.

class Ship:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return f'Модель корабля {self.__model}'

    def sail(self):
        print('Корабль плывёт...')


class CargoShip(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.tonnage_load = 0

    def load(self, value):
        print('Загружаем')
        self.tonnage_load += value
        print(f'Текущая загруженность: {self.tonnage_load}')

    def unload(self, value):
        print('Выгружаем...')
        if self.tonnage_load > 0 and self.tonnage_load - value >= 0:
            self.tonnage_load -= value
            print(f'Текущая загруженность: {self.tonnage_load}')
        else:
            print('Выгрузка такого значения невозможна!')


class WarShip(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print(f'Корабль атакует с помощью {self.gun}!')


ship_1 = WarShip('Варяг-228', 'Аркибуза')
ship_1.attack()
ship_2 = CargoShip('Мирный-666')
ship_2.load(900)
ship_2.unload(800)
ship_2.unload(150)
