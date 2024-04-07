def is_palindrom(x):
    str_dig = str(x)
    if str_dig == str_dig[::-1]:
        return True
    else:
        return False


x = -5
print(is_palindrom(x))
