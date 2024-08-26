# Задача 1. Сэндвич
# Есть функция, которая выводит начинку сэндвича. Сверху и снизу от начинки идут различные ингредиенты вроде салата,
# помидоров и других. Всё это в свою очередь содержится между двух половинок булочки. Реализуйте такую функцию и два
# соответствующих декоратора — ингредиенты и хлеб.

# Пример результата работы программы при вызове функции sandwich:
# </----------\>
#  #помидоры#
# --ветчина--
#   ~салат~
#  <\______/>

def get_some_salad(func):
    def wrapped_func(*args, **kwargs):
        print('   помидоры')
        func(*args, **kwargs)
        print('    салат')
    return wrapped_func


def get_some_buns(func):
    def wrapped_func(*args, **kwargs):
        print('</----------\>')
        func(*args, **kwargs)
        print('  <\______/>')
    return wrapped_func


@get_some_buns
@get_some_salad
def filling_burger(filler):
    print(filler)


filling_burger("   ветчина")
