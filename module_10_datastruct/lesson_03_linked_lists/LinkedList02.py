class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
        self.head = new_node
        print(f'Начало списка: {self.head.data}')

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            # return self.insert_at_head(data)
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node
        print(f'Конец списка: {self.tail.data}')

    def remove_from_head(self):
        removed_node = self.head
        self.head = self.head.next_node
        self.head.prev_node = None
        print(f'Начало списка: {self.head.data}')
        return removed_node.data

    def remove_from_tail(self):
        removed_node = self.tail
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        print(f'Конец списка: {self.tail.data}')
        return removed_node.data

    def print_ll_from_head(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        print(f'Список выведен сначала')

    def print_ll_from_tail(self):
        current_node = self.tail
        while current_node:
            print(current_node.data)
            current_node = current_node.prev_node
        print(f'Список выведен c конца')


if __name__ == '__main__':
    double_ll = DoubleLinkedList()
    double_ll.insert_at_head('data_01')
    double_ll.insert_at_head('data_00')
    double_ll.insert_at_tail('data_02')
    double_ll.insert_at_tail('data_03')
    double_ll.print_ll_from_head()
    print()
    double_ll.print_ll_from_tail()
    print()
    double_ll.remove_from_head()
    double_ll.remove_from_tail()
    double_ll.print_ll_from_head()
    print()
    double_ll.print_ll_from_tail()
    print()
