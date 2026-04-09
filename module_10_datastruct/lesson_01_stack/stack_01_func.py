def push(val):
    stack.append(val)


def pop():
    val = stack.pop()
    return val


def peek():
    print(stack[-1])


if __name__ == '__main__':
    stack = []
    push(3)
    push(2)
    push(1)

    peek()

    print(pop())
    print(pop())
    print(pop())
