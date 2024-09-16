import fileinput
import math

primes = set()
result = 0


def is_prime(n):
    if n < 2:
        return False
    if n in primes:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    primes.add(n)
    return True


for line in fileinput.input():
    l, r = map(int, line.strip().split())
    for i in range(l, r + 1):
        if is_prime(i):
            continue
        counter = 0
        for j in range(1, i + 1):
            if i % j == 0:
                counter += 1
        if is_prime(counter):
            result += 1

print(result)