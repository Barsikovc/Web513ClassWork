import copy


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    """
    Класс созданный для работы со структурой данных Стек
    Помимо стандартных методов push и pop,
    реализованы....
    """
    def __init__(self, stack_size, top=None):
        self.top = top
        self.stack_size = stack_size
        self.counter = 0

    def push(self, data):
        """
        Метод для добавления данных в стек.
        Данные будут добавлены только если пройдена проверка на размер стека.
        :param data:
            данные, любого типа
        :return:
            None
        """
        if self.counter < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top
            self.top = new_node
            self.counter += 1
        else:
            print(f'Stack overflow! Max items: {self.stack_size}')

    def pop(self):
        remove_last = self.top
        self.top = self.top.next_node
        self.counter -= 1
        return remove_last.data

    @classmethod
    def counter_int(cls, stack):
        if isinstance(stack, Stack):
            temp_stack = copy.copy(stack)
            counter_int = 0
            while not cls.is_empty(temp_stack):
                if isinstance(temp_stack.top.data, int):
                    counter_int += 1
                temp_stack.pop()
            return counter_int
        print(f'Объект неподходящего класса')
        return None

    @staticmethod
    def is_empty(stack):
        if not stack.top:
            return True
        return False


if __name__ == '__main__':
    stack = Stack(stack_size=4)
    stack.push(1)
    stack.push('str')
    stack.push(3)
    stack.push(0.5)
    stack.push('str2')
    print(Stack.counter_int(stack))
    print()

    # просто для примера объект другого класса
    node = Node('data')
    print(Stack.counter_int(node))
