import pickle


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
    my_ll = DoubleLinkedList()
    my_ll.insert_at_head("Барсик_01")
    my_ll.insert_at_head("Снежок_00")
    my_ll.insert_at_tail('Франц_03')
    my_ll.print_ll_from_head()
    print(my_ll)
    print()

    with open('pickled_data.cats', 'wb') as file:
        pickle.dump(my_ll, file)

    try:
        with open('pickled_data.cats', 'rb') as file:
            my_data_ff = pickle.load(file)
        print(my_data_ff)
    except FileNotFoundError:
        print(f'Файл не найден')
    except Exception as ex:
        print(ex)
    else:
        my_data_ff.print_ll_from_head()
