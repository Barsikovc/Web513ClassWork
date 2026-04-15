class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        dequeue_item = self.head
        self.head = self.head.next_node
        return dequeue_item.data

    def peek_first(self):
        if not self.head:
            print(f'Очередь пуста')
        else:
            print(self.head.data)

    def peek_last(self):
        if not self.head:
            print(f'Очередь пуста')
        else:
            print(self.tail.data)

    def len_queue(self):
        counter = 0
        if not self.head:
            return counter
        current_node = self.head
        while current_node:
            counter += 1
            current_node = current_node.next_node
        return counter


if __name__ == '__main__':
    my_node = Node('item_0')
    queue = Queue(my_node, my_node)

    for i in range(1, 6):
        queue.enqueue(f'item_{i}')

    print(queue.len_queue())
    queue.peek_first()
    queue.peek_last()
    print()

    while True:
        q_data = queue.dequeue()
        if not q_data:
            break
        else:
            print(q_data)
