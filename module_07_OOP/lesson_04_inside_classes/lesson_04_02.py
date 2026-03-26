class Classy:
    pass


if __name__ == '__main__':
    print(Classy.__name__)
    print(type('строка').__name__)
    classy_obj = Classy()
    print(type(classy_obj).__name__)
