# Задача 1. Налоги
# Что нужно сделать
# Реализуйте иерархию классов, описывающих имущество налогоплательщиков. Она должна состоять из базового класса Property
# и производных от него классов Apartment, Car и CountryHouse.

# Базовый класс должен иметь атрибут worth (стоимость), который передаётся в конструктор, и метод расчёта налога,
# переопределённый в каждом из производных классов. Налог на квартиру вычисляется как 1/1000 её стоимости,
# на машину — 1/200, на дачу — 1/500.

# Каждый дочерний класс должен иметь конструктор с одним параметром, передающий свой параметр конструктору базового
# класса.

# Разработайте интерфейс программы. Пусть она запрашивает у пользователя количество его денег и стоимость имущества, а
# затем выдаёт налог на соответствующее имущество и показывает, сколько денег ему не хватает (если это так).

# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
# При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
# Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
# Для создания нового класса на основе уже существующего используется наследование.
# Сообщения о процессе получения результата осмысленны и понятны пользователю.
# Переменные, функции и собственные методы классов имеют значащие имена, а не a, b, c, d.
# Классы и методы/функции имеют прописанную документацию.

class Property:
    def __init__(self, worth):
        self.worth = worth

    def calculate_tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 10000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 500


total_money = int(input('Введите количество денег: '))
price_apartment = int(input('Стоимость апартаментов: '))
price_car = int(input('Стоимость машины: '))
price_house = int(input('Стоимость дома: '))

user_apartment = Apartment(price_apartment)
user_car = Car(price_car)
user_house = CountryHouse(price_house)

total_cost = (price_apartment + user_apartment.calculate_tax()) + (price_car + user_car.calculate_tax()) + (
            price_house + user_house.calculate_tax())

print(f'Налог на апартаменты: {round(user_apartment.calculate_tax(), 2)}\n'
      f'Налог на машину: {round(user_car.calculate_tax(), 2)}\n'
      f'Налог на загородный дом: {round(user_house.calculate_tax(), 2)}\n'
      f'Общая стоимость имущества с учетом налогов составляет : {round(total_cost, 2)}\n')

if total_money >= total_cost:
    print('Вам хватает денег!')
else:
    print(f'Вам не хватило: {round(total_cost - total_money, 2)}.')
