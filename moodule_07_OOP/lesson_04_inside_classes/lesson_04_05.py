class SuperOne:
    pass


class SuperMixin:
    pass


class Sub(SuperMixin, SuperOne):
    pass


class SubSub(Sub):
    pass


def print_bases(cls):
    print('(', end=' ')
    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


if __name__ == '__main__':
    print_bases(SubSub)
    print_bases(Sub)
    print_bases(SuperMixin)
    print_bases(SuperOne)
