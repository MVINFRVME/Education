# Задача 3. Гистограмма частоты
# Лингвистам нужно собрать данные о частоте букв в тексте, исходя из этих данных будет строиться гистограмма частоты
# букв. Напишите программу, которая получает сам текст и считает, сколько раз в строке встречается каждый символ.
# На экран нужно вывести содержимое в виде таблицы, отсортированное по алфавиту, а также максимальное значение частоты.
# Пример:
# Введите текст: Здесь что-то написано
#   : 2
# - : 1
# З : 1
# а : 2
# д : 1
# е : 1
# и : 1
# н : 2
# о : 3
# п : 1
# с : 2
# т : 2
# ч : 1
# ь : 1
# Максимальная частота: 3

text = input("Введите текст: ").lower()
sym_dict = dict()

for sym in text:
    if sym in sym_dict:
        sym_dict[sym] += 1
    else:
        sym_dict[sym] = 1

for i_sym in sorted(sym_dict.keys()):
    print(f"{i_sym} : {sym_dict[i_sym]}")

print(f"Максимальная частота: {max(sym_dict.values())}")
