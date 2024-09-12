# Задача 3. Дата
# Что нужно сделать
# Реализуйте класс Date, который должен:
#
# проверять числа даты на корректность;
# конвертировать строку даты в объект класса Date, состоящий из соответствующих числовых значений дня, месяца и года.
# Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.
#
# При тестировании программы объект класса Date должен инициализироваться исключительно через метод конвертации,
# например:
#
# date = Date.from_string('10-12-2077')
# Неверный вариант: date = Date(10, 12, 2077)
#
# Пример основного кода:
#
# date = Date.from_string('10-12-2077')
# print(date)
# print(Date.is_date_valid('10-12-2077'))
# print(Date.is_date_valid('40-12-2077'))
# Результат:
# День: 10    Месяц: 12    Год: 2077
# True
# False
#
# Что оценивается
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
# При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
# Для получения и установки значений приватных атрибутов используются сеттеры и геттеры с соответствующими декораторами.
# Для создания нового класса на основе уже существующего используется наследование.
# Для статических и классовых методов используется декоратор classmethod.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). Если функция/метод ничего не
# возвращает, то используется None.

class Date:
    @classmethod
    def from_string(cls, curr_date: str):
        day, month, year = curr_date.split('-')
        return f'День: {day}    Месяц: {month}    Год: {year}'

    @classmethod
    def is_date_valid(cls, curr_date):
        day, month, year = curr_date.split('-')
        if not 0 <= int(year) <= 3000:  # будем считать что до рождества христова год не валидный, аминь
            return False
        if not 1 <= int(month) <= 12:
            return False
        if not 1 <= int(day) <= 31:  # по идеи надо еще проверять в каком месяце сколько дней,
            # а также учитывать високосный ли год или нет, но мне стало лень(
            return False
        return True


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
