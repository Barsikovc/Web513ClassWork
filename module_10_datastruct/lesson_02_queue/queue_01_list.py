queue = []


def enqueue(data):
    queue.append(data)


def dequeue():
    if not queue:
        print(f'Очередь пуста!')
        return None
    return queue.pop(0)


def peek_first():
    if not queue:
        print(f'Очередь пуста')
    else:
        print(queue[0])


def peek_last():
    if not queue:
        print(f'Очередь пуста')
    else:
        print(queue[-1])


def size():
    print(len(queue))


if __name__ == '__main__':
    enqueue('data_1')
    enqueue('data_2')
    enqueue('data_3')
    enqueue('data_4')
    peek_first()
    peek_last()
    size()
    print(dequeue())
    print(dequeue())
    print(dequeue())
    print(dequeue())
    print(dequeue())

