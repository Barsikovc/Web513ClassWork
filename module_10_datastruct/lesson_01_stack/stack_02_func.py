def push(stack, val):
    stack.append(val)


def pop(stack):
    if stack:
        val = stack.pop()
        return val
    return None


def peek(stack):
    if stack:
        print(stack[-1])
    else:
        print('Stack is empty')


if __name__ == '__main__':
    stack1 = []
    stack2 = []

    push(stack1, 1)
    push(stack1, 2)
    push(stack1, 3)

    peek(stack1)

    while stack1:
        val = pop(stack1)
        if val:
            push(stack2, val)

    peek(stack2)
    print(stack2)
