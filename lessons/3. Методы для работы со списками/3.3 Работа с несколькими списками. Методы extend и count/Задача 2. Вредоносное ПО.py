# Гера решил попрактиковаться в программировании и захотел написать небольшой скрипт, который после двух сообщений
# отправляет ещё одно на основе первых двух.
#
# Пользователь вводит две строки. В каждой из них есть какое-то количество специальных символов ! и ?.
# Напишите программу, которая считает количество этих символов отдельно в первой строке и отдельно во второй.
# Если в первой строке их больше, чем во второй, то на экран выводится первая строчка, объединённая со второй,
# а иначе — вторая с первой. При равном количестве символов в строках выводится «Ой».

first_message = input("Первое сообщение: ")
second_message = input("Второе сообщение: ")

first_message_count = first_message.count("!") + first_message.count("?")
second_message_count = second_message.count("!") + second_message.count("?")

print("Третье сообщение: ", end="")

if first_message_count > second_message_count:
    print(f"{first_message}{second_message}")
elif first_message_count < second_message_count:
    print(f"{second_message}{first_message}")
else:
    print("Ой")

# Решение учителя

# first_word = input("Первое сообщение: ")
# second_word = input("Первое сообщение: ")
# first_count = first_word.count("!") + first_word.count("?")
# second_count = second_word.count("!") + second_word.count("?")
# if first_count < second_count:
#     first_word, second_word = second_word, first_word  # пусть первым словом будет то, в котором больше знаков
#
# print(first_word + second_word)
