items = input("Введите предметы: ")
item_list = list(items)

count = 0
index = 0

for i in item_list:
    if i == ":":
        item_list[index] = ";"
        count += 1
    index += 1

print("Исправленная строка:", end=" ")

for symbol in item_list:
    print(symbol, end="")

print(f"\nКол-во замен: {count}")
