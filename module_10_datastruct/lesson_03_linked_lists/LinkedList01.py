class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node

    def insert_at_index(self, data, node_idx):
        if node_idx == 0:
            return self.insert_at_head(data)
        elif node_idx > self.len_ll() - 1:
            return self.insert_at_tail(data)
        new_node = Node(data)
        current_node = self.head
        current_node_idx = 0
        while current_node and current_node_idx < node_idx - 1:
            current_node = current_node.next_node
            current_node_idx += 1
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        return True

    def print_ll(self):
        if not self.head:
            print('Список пуст')
            return False  # для тестирования
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        print('Информация выведена')
        return True  # для тестирования

    def remove_from_head(self):
        if not self.head:
            print(f'Список пуст')
            return None
        removed_node = self.head
        # self.head = removed_node.next_node
        self.head = self.head.next_node
        print(f'Удалили {removed_node.data}. Теперь начало: {self.head.data}')
        return removed_node.data

    def remove_node_by_idx(self, rm_idx):
        if rm_idx == 0:
            return self.remove_from_head()
        current_node = self.head
        current_node_idx = 0
        while current_node and current_node_idx < rm_idx - 1:
            current_node = current_node.next_node
            current_node_idx += 1
        if current_node is None or current_node.next_node is None:
            print(f'Ничего не удалили. Начало: {self.head.data}')
            return None
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node
        print(f'Удалили {removed_node.data}. Начало {self.head.data}')
        return removed_node.data

    def remove_node_by_data(self, rm_data):
        if rm_data == self.head.data:
            return self.remove_from_head()
        current_node = self.head
        while current_node and current_node.next_node:
            # print(current_node.data, current_node.next_node.data)
            if current_node.next_node.data == rm_data:
                removed_node = current_node.next_node
                current_node.next_node = current_node.next_node.next_node
                print(f'Удалили {removed_node.data}. Начало: {self.head.data}')
                return removed_node.data
            current_node = current_node.next_node
        print(f'Ничего не удалили. Начало: {self.head.data}')
        return None

    def contains(self, data):
        current_node = self.head
        while current_node:
            if data == current_node.data:
                print(f'Элемент: {data} найден')
                return True
            current_node = current_node.next_node
        print(f'Элемент: {data} НЕ найден')
        return False

    def get_from_ll_by_idx(self, node_idx):
        len_ll = self.len_ll()
        if node_idx > len_ll - 1:
            print(f'В списке нет такого индекса, максимальный индекс = {len_ll - 1}')
            return None
        current_node = self.head
        current_node_idx = 0
        while current_node_idx <= node_idx:
            if current_node_idx == node_idx:
                return current_node.data
            current_node = current_node.next_node
            current_node_idx += 1
        return None

    def len_ll(self):
        items_count = 0
        current_node = self.head
        while current_node:
            items_count += 1
            current_node = current_node.next_node
        return items_count


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.print_ll()
    linked_list.insert_at_tail('data_02')
    linked_list.insert_at_tail('data_03')
    linked_list.insert_at_head('data_01')
    linked_list.insert_at_head('data_00')
    linked_list.insert_at_tail('data_04')
    linked_list.insert_at_index('idx', 3)
    linked_list.print_ll()

    linked_list.contains('data_02')
    linked_list.contains('data_05')
    print(linked_list.len_ll())
    print(linked_list.get_from_ll_by_idx(5))
    print(linked_list.get_from_ll_by_idx(2))
    print()
    linked_list.print_ll()
    linked_list.remove_node_by_idx(2)
    linked_list.print_ll()
    print()
    #
    linked_list.remove_node_by_data('data_03')
    linked_list.print_ll()
