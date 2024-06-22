from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.appendleft(3)
print(queue)
item = queue.popleft()
print(item)

from collections import namedtuple
print()
point = namedtuple('point', ['x', 'y', 'z'])
p = point(2, 3, 4)
print(p.x)
print(p.y)
print(p)

from collections import Counter
print()
data = [1, 2, 3, 1, 2, 1, 3, 4, 5, 4, 2, 1]
counter = Counter(data)
print(counter) # Вывод: Counter({1: 4, 2: 3, 3: 2, 4: 2, 5: 1})
print(counter[1]) # Вывод: 4 (количество вхождений элемента 1)
most_common = counter.most_common(2)
print(most_common) # Вывод: [(1, 4), (2, 3)] (наиболее часто встречающиеся элементы)


from collections import defaultdict
# Создание defaultdict со значением по умолчанию — пустым списком
d = defaultdict(list)
d['apple'].append('red') # Добавление значения 'red' к ключу 'apple'
d['banana'].append('yellow') # Добавление значения 'yellow' к ключу 'banana'
d['apple'].append('green') # Добавление значения 'green' к ключу 'apple'
print(d) # Вывод: defaultdict(<class 'list'>, {'apple': ['red', 'green'], 'banana': ['yellow']})
print(d['apple']) # Вывод: ['red', 'green']
print(d['banana']) # Вывод: ['yellow']
print(d['cherry']) # Вывод: [] (пустой список, значение по умолчанию)
print(d) # Вывод: defaultdict(<class 'list'>, {'apple': ['red', 'green'], 'banana': ['yellow'], 'cherry': []})
