
def t(n):
    for i in range(2, n - 2):
        st = str(i)
        b = int(n, i)
        if str(i) != str(i)[::-1]:
            return False
    else:
        return True

print(t(9))