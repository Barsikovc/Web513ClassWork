class Stack:
    def __init__(self):
        self.__stack = []

    @property
    def stack(self):
        return self.__stack

    def push(self, val):
        if val:
            self.stack.append(val)
        else:
            print(f'Невозможно поместить None в стек')

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            return val
        print(f'Стек пуст')
        return None

    def peek(self):
        if self.stack:
            print(f'На вершине стека: {self.stack[-1]}')
        else:
            print(f'Стек пуст')

    def __str__(self):
        return f'Содержимое стека: {self.stack}'


if __name__ == '__main__':
    stack1 = Stack()
    stack2 = Stack()

    stack1.push(3)
    stack1.push(2)
    stack1.push(1)

    stack1.peek()
    print(stack1)
    print()

    stack2.push(stack1.pop())
    stack2.push(stack1.pop())
    stack2.push(stack1.pop())
    stack2.push(stack1.pop())
    stack2.push(stack1.pop())

    print(stack1)
    print(stack2)
    print()

    stack2.peek()
    print(stack2.pop())
    print(stack2.pop())
    print(stack2.pop())
    print(stack2.pop())
