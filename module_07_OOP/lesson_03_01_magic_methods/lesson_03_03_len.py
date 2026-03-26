class Group:

    def __init__(self, members):
        self.members = members

    # должен возвращать ЦЕЛОЕ число
    def __len__(self):
        return len(self.members)


if __name__ == '__main__':
    group = Group(['Иван', 'Мария', 'Петр'])
    print(len(group))
