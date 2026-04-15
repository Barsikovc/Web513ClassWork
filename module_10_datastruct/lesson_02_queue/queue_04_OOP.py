class Queue:
    def __init__(self, queue: list = None):
        if not queue:
            self.__queue = []
        else:
            self.__queue = queue

    @property
    def queue(self):
        return self.__queue

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.queue:
            print(f'Очередь пуста')
            return None
        else:
            return self.queue.pop(0)

    def peek_first(self):
        if not self.queue:
            print(f'Очередь пуста')
        else:
            print(self.queue[0])

    def peek_last(self):
        if not self.queue:
            print(f'Очередь пуста')
        else:
            print(self.queue[-1])

    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    queue1 = Queue(['data_0'])
    queue1.enqueue('data_1')
    queue1.enqueue('data_2')
    queue1.enqueue('data_3')
    queue1.enqueue('data_4')
    print(queue1.queue)
    print(queue1.size())
    queue1.peek_first()
    queue1.peek_last()
    for i in range(queue1.size()):
        print(queue1.dequeue())
