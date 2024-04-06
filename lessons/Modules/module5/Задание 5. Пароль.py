# Задание 5. Пароль
# Что нужно сделать
# При регистрации на сайте, помимо логина, нужно придумать пароль. Этот пароль должен состоять минимум из восьми
# символов, содержать хотя бы одну большую букву и не менее трёх цифр. Тогда он будет считаться надёжным.
#
# Напишите программу, которая просит пользователя придумать пароль до тех пор, пока этот пароль не станет надёжным.
# Должна использоваться латиница.
#
# Пример
#
# Придумайте пароль: qwerty.
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Придумайте пароль: qwerty12.
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Придумайте пароль: qwerty123.
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Придумайте пароль: qWErty123.
# Это надёжный пароль.

while True:
    password = input('Придумайте пароль: ')
    digit_count = 0
    upper_count = 0

    for sym in password:
        if sym.isdigit():
            digit_count += 1
        elif sym.isupper():
            upper_count += 1

    if digit_count >= 3 and upper_count >= 1 and len(password) >= 8:
        print('Это надёжный пароль.')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
