class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    # def pop(self):
    #     if self.top:
    #         remove_last = self.top
    #         # self.top = remove_last.next_node
    #         self.top = self.top.next_node
    #         return remove_last.data
    #     return None

    def pop(self):
        remove_last = self.top
        self.top = self.top.next_node
        return remove_last.data


if __name__ == '__main__':
    # node_1 = Node('2 RUB')
    # node_2 = Node('5 RUB', node_1)
    # node_3 = Node('10 RUB', node_2)
    #
    # print(node_1.data)
    # print(node_2.data)
    # print(node_3.next_node.next_node.data)
    # #             >> node2  >> node1

    stack = Stack()
    stack.push('2 RUB')
    stack.push('5 RUB')
    stack.push('10 RUB')

    # print(stack.top.data)
    # print(stack.top.next_node.data)
    # print(stack.top.next_node.next_node.data)

    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())

    # # для pop под решеткой (условно безопасный)
    # for i in range(10):
    #     try:
    #         data = stack.pop()
    #         if not data:
    #             raise AttributeError
    #         print(data)
    #     except AttributeError:
    #         print('Stack is Empty')
    #         break
    # print('Data Extracted')

    # для pop обычного
    for i in range(10):
        try:
            print(f'{stack.pop()}')
        except AttributeError:
            print('Stack is Empty')
            break
    print('Data extracted')
