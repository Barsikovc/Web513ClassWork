def push(stack, val):
    stack.append(val)


def pop(stack):
    try:
        val = stack.pop()
    except IndexError:
        return None
    else:
        return val


def peek(stack):
    if stack:
        print(stack[-1])
    else:
        print('Stack is empty')


if __name__ == '__main__':
    my_stack = []
    push(my_stack, 3)
    push(my_stack, 2)
    push(my_stack, 1)

    my_stack[0] = 0
    print(pop(my_stack))
    print(pop(my_stack))
    print(pop(my_stack))
    print(pop(my_stack))
    print(pop(my_stack))