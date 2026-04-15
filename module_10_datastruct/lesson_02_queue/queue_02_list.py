def enqueue(queue, data):
    queue.append(data)


def dequeue(queue):
    if not queue:
        print(f'Очередь пуста!')
        return None
    return queue.pop(0)


def peek_first(queue):
    if not queue:
        print(f'Очередь пуста')
    else:
        print(queue[0])


def peek_last(queue):
    if not queue:
        print(f'Очередь пуста')
    else:
        print(queue[-1])


def size(queue):
    print(len(queue))
    return len(queue)


if __name__ == '__main__':
    queue1 = []
    queue2 = []
    enqueue(queue1, 'data_1')
    enqueue(queue1, 'data_2')
    enqueue(queue1, 'data_3')
    enqueue(queue1, 'data_4')
    # print(queue1)

    for i in range(size(queue1)):
        enqueue(queue2, dequeue(queue1))

    peek_first(queue2)
    peek_last(queue2)

