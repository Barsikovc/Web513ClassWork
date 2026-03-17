class Group:
    group = []

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Group.group.append(self)

    # должен возвращать ЦЕЛОЕ число
    @classmethod
    def __len__(cls):
        return len(cls.group)


if __name__ == '__main__':
    group_member1 = Group('Петр', 'Петров')
    group_member2 = Group('Иван', 'Иванов')
    group_member3 = Group('Сергей', 'Сергеев')

    print(Group.group)
    print(len(Group.group))
