class MyClass:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.i = 3
        self.ireal = 3.5
        self.integer = 4
        self.z = 5


def inc_ints_i_start(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


if __name__ == '__main__':
    my_obj = MyClass()
    print(my_obj.__dict__)
    inc_ints_i_start(my_obj)
    print(my_obj.__dict__)
