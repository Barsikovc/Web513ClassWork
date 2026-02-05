class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print('__iter__')
        return self

    def __next__(self):
        print('__next__')
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


class Class(Fib):
    def __init__(self, nn):
        super().__init__(nn)


if __name__ == '__main__':
    my_fib = Class(10)

    for i in my_fib:
        print(i)
