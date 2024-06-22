# Задача 1. Юниты
# Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты). У Юнита есть действие
# «получить урон» (базовый класс получает 0 урона).

# Также есть два дочерних класса:

# Солдат: получает урон, равный переданному значению.
# Обычный гражданин: получает урон, равный двукратному переданному значению.
# Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма
# (а также инкапсуляции и наследования, конечно же).

class Unit:
    def __init__(self, hp):
        self.__hp = hp

    def set_hp(self, amount):
        self.__hp = amount

    def get_hp(self):
        return self.__hp

    def get_dmg(self, amount):
        self.set_hp(self.get_hp())


class Soldier(Unit):
    def get_dmg(self, amount):
        self.set_hp(self.get_hp() - amount)


class Citizen(Unit):
    def get_dmg(self, amount):
        self.set_hp(self.get_hp() - amount * 2)


soldat = Soldier(250)
soldat.set_hp(230)
print(soldat.get_hp())
soldat.get_dmg(20)
print(soldat.get_hp())

chel = Citizen(100)
print(chel.get_hp())
chel.get_dmg(20)
print(chel.get_hp())





