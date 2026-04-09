from stack_04_OOP import Stack


class AddingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__stack_sum = 0

    @property
    def stack_sum(self):
        return self.__stack_sum

    def push(self, val):
        if isinstance(val, (int, float)):
            self.__stack_sum += val
            super().push(val)

    def pop(self):
        val = super().pop()
        if val:
            self.__stack_sum -= val
        return val

    def __str__(self):
        return f'Содержимое стека: {self.stack}. Сумма значений {self.stack_sum}'


if __name__ == '__main__':
    stack = AddingStack()
    for i in range(1, 5):
        stack.push(i)

    print(stack)
    for i in range(6):
        val = stack.pop()
        if val:
            print(f'Извлечено {val}. {stack}')
        else:
            break
