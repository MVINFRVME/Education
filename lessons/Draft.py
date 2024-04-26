import sys
import copy

b = (1, 2, 3)
a = [1, 2, 3]
print("Размер списка a в памяти:", sys.getsizeof(a), "байт")
print("Размер списка a в памяти:", sys.getsizeof(b), "байт")


ab = [1, [2, 4], 3]
ac = ab.copy()
print(ab)
print(ac)
ab[1][1] = 3
print(ab)
print(ac)

print(id('2'))



