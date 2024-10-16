# Задача 2. Непонятно!
# Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами, ссылками, объектами и их id. Видя, как он
# мучается, вы решили помочь ему и объяснить эту тему наглядно.
# Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип введённых данных, информацию о его
# изменяемости, а также id этого объекта.
# Помните, что через input можно получить только строку, что бы вы ни вводили. В данном случае ввод можно выполнить
# вручную, просто вписав нужный объект в переменную, без использования функции input.
#
# Пример 1:
# Введите данные: привет
# Тип данных: str (строка)
# Неизменяемый (immutable)
# Id объекта: 1705156583984
#
# Пример 2:
# Введите данные: {‘a’: 10, ‘b’: 20}
# Тип данных: dict (словарь)
# Изменяемый (mutable)
# Id объекта: 1705205308536


def is_mutable(value):
    if isinstance(value, dict) or isinstance(value, list) or isinstance(value, set):
        return 'Изменяемый (mutable)'
    else:
        return 'Неизменяемый (immutable)'


def what_type(value, struct):
    data_type = str(type(value))
    if data_type in struct:
        return struct[data_type]


type_dict = {"<class 'str'>": 'str (строка)',
             "<class 'dict'>": 'dict (словарь)',
             "<class 'int'>": 'int (целое число)'}  # Можно написать и другие типы данных


info = 'привет'

print(f'Тип данных {what_type(info, type_dict)}\n'
      f'{is_mutable(info)}\n'
      f'ID объекта: {id(info)}')
