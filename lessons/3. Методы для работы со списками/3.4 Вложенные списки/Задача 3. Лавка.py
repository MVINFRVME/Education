goods = [
    ["яблоки", 50],
    ["апельсины", 190],
    ["груши", 100],
    ["нектарины", 200],
    ["бананы", 77],
]

fruit_name = input("Новый фрукт: ")
price = int(input("Цена: "))

goods.append([fruit_name, price])
for good in goods:
    good[1] = round(good[1] * 1.08, 2)

print(goods)
