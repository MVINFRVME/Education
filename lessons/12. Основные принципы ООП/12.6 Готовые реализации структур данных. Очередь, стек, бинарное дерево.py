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

from queue import Queue

# Создание экземпляра очереди
q = Queue()
# Добавление элементов в очередь
q.put(1)
q.put(2)
q.put(3)
# Получение и удаление элемента из очереди
item = q.get()
print(item) # Вывод: 1
# Проверка, пуста ли очередь
is_empty = q.empty()
print(is_empty) # Вывод: False
# Получение размера очереди
size = q.qsize()
print(size) # Вывод: 2
# Очистка очереди
q.queue.clear()
# Проверка, пуста ли очередь после очистки
is_empty = q.empty()
print(is_empty) # Вывод: True

from queue import LifoQueue

# Создание экземпляра стека
stack = LifoQueue()
# Добавление элементов в стек
stack.put(1)
stack.put(2)
stack.put(3)
# Получение и удаление элемента из стека
item = stack.get()
print(item) # Вывод: 3
# Проверка, пуст ли стек
is_empty = stack.empty()
print(is_empty) # Вывод: False
# Получение размера стека
size = stack.qsize()
print(size) # Вывод: 2
# Очистка стека
stack.queue.clear()
# Проверка, пуст ли стек после очистки
is_empty = stack.empty()
print(is_empty) # Вывод: True

class Node:
    def __init__(self, data, next=None):
        # Конструктор узла
       self.data = data  # Значение узла
       self.next = next   # Ссылка на следующий узел
# Для этого нам надо создать корневой элемент
first = Node(123)
# И следующий элемент, который будет ссылаться на корневой
second = Node(456, first)
# Получаются два отдельных объекта, которые при этом связаны ссылкой (второй объект ссылается на первый)

class Node:
    def __init__(self, key):
        # Конструктор узла
        self.key = key
        self.left = None
        self.right = None

# Пример создания бинарного дерева
root = Node(10) # Создаём корневой узел
root.left = Node(2) # Добавляем левый дочерний узел
root.right = Node(15) # Добавляем правый дочерний узел

# Визуализация бинарного дерева:
# 10
# / \
# 2 15

# binarytree
# binarytree — это модуль, который позволяет создавать и визуализировать бинарные деревья и работать с их различными типами. 
# Он позволяет легко создавать случайные бинарные деревья и обеспечивает методы для их обхода, поиска и других операций.
# Для установки модуля binarytree вы можете использовать менеджер пакетов pip. Откройте терминал и выполните следующую команду:
# pip install binarytree
# После успешной установки вы можете начать использовать модуль binarytree. 
# Посмотрите пример кода, демонстрирующий создание и работу с бинарным деревом с использованием binarytree:

from binarytree import Node

# Создание бинарного дерева вручную
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)

# Вывод структуры дерева
print("Структура бинарного дерева:")
print(root)

# Обход дерева в прямом порядке (preorder)
def preorder(node):
    if node is not None:
        print(node.value)
        preorder(node.left)
        preorder(node.right)

print("Обход дерева в прямом порядке (preorder):")
preorder(root)

# Поиск элемента в дереве
def search(node, value):
    if node is None or node.value == value:
        return node
    if value < node.value:
        return search(node.left, value)
    return search(node.right, value)

print("Поиск элемента в дереве:")
result = search(root, 7)
if result is not None:
    print("Элемент найден!")
else:
    print("Элемент не найден!")
