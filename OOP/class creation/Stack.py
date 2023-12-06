# Напишите определение класса Stack
class Stack:
    def __init__(self):
        self.values = []

    # Метод push(item) добавляет новый элемент на вершину стека, метод ничего не возвращает
    def push(self, item):
        pass

    # Метод pop() удаляет верхний элемент из стека. Метод ***возвращает элемент***

    def pop(self):
        pass

   # Возвращает верхний элемент стека, но не удаляет его.

    def peek(self):
        pass

   # Метод is_empty() проверяет стек на пустоту. Возвращает булево значение
    def is_empty(self):
        pass

    # Метод size() возвращает количество элементов в стеке.
    def size(self):
        return len(self.values)

# Ниже код для проверки класса Stack
s = Stack()
assert s.values == []
assert isinstance(s, Stack)

s.peek()  # распечатает 'Empty Stack'
assert s.is_empty() is True
s.push('cat')
assert s.size() == 1
assert s.peek() == 'cat'

s.push('dog')
assert s.size() == 2
assert s.peek() == 'dog'

s.push(True)
assert s.size() == 3
assert s.is_empty() is False

s.push(777)
assert s.size() == 4

assert s.pop() == 777
assert s.size() == 3

assert s.pop() is True
assert s.size() == 2

s.push(123)
s.push(123456)
assert s.peek() == 123456
assert s.size() == 4

assert s.pop() == 123456
assert s.pop() == 123
assert s.pop() == 'dog'
assert s.is_empty() is False
assert s.pop() == 'cat'
assert s.is_empty() is True

d = Stack()
assert d.peek() is None  # Печатает "Empty Stack"
assert d.pop() is None  # Печатает "Empty Stack"
d.push('hello')
assert d.size() == 1
d.push('world')
assert d.size() == 2
assert d.peek() == 'world'
assert d.pop() == 'world'
assert d.peek() == 'hello'
