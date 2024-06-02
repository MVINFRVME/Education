# Задача 2. Семья
# Реализуйте класс «Семья», который состоит из атрибутов «Имя», Деньги» и «Наличие дома» и объекты которого могут
# выполнять следующие действия:

# Отобразить информацию о себе.
# Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»). Вывести соответствующее сообщение об
# успешной/неуспешной покупке дома.
# Создайте как минимум один экземпляр класса и проверьте работу методов.

# Пример работы программы (вывод информации, покупка дома, заработок, очередная покупка):
# Family name: Common family
# Family funds: 100000
# Having a house: False

# Try to buy a house
# Not enough money!

# Earned 800000 money! Current value: 900000
# Try to buy a house again
# House purchased! Current money: 0.0

# Family name: Common family
# Family funds: 0.0
# Having a house: True

class Family:
    surname = 'Common family'
    funds = 100000
    having_a_house = False

    def show_info(self):
        print('\nFamily name: {}\n'
              'Family funds: {}\n'
              'Having a house: {}\n'
              .format(self.surname, self.funds, self.having_a_house))

    def earn_money(self, money):
        self.funds += money
        print('Earned {} money! Current value: {}'.format(money, self.funds))

    def buy_house(self, price, discount=0):
        price -= price * discount / 100
        if self.funds >= price:
            self.funds -= price
            self.having_a_house = True
        else:
            print('Not enough money!\n')


my_family = Family()
my_family.show_info()

print('Try to buy a house')
my_family.buy_house(120000)

print('Try to buy a house again')
my_family.earn_money(800000)
my_family.buy_house(120000, 10)

my_family.show_info()

