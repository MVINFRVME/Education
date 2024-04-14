number_of_packs = int(input("Кол-во пакетов: "))
final_pack_list = []
total_lost_packs = 0

for pack in range(number_of_packs):
    print(f"\nПакет номер {pack + 1}")
    pack_list = []

    for i in range(4):
        bit = int(input(f"{i + 1} бит: "))
        pack_list.append(bit)

    if pack_list.count(-1) <= 1:
        final_pack_list.extend(pack_list)
    else:
        print("Много ошибок в пакете")
        total_lost_packs += 1


print(
    f"\nПолученное сообщение: {final_pack_list}\n"
    f"Кол-во ошибок в сообщении: {final_pack_list.count(-1)}\n"
    f"Кол-во потерянных пакетов: {total_lost_packs}"
)
