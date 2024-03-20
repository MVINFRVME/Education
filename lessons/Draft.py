test = [1, 2, 3]
print(id(test)) # Здесь вы увидите один айди
test = test[::-1]
print(id(test)) # А здесь уже другой
