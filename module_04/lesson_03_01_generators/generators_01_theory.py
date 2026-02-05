def my_generator():
    yield 1
    yield 2
    yield 3


if __name__ == '__main__':
    gen_obj = my_generator()
    print(gen_obj)
    print(next(gen_obj))
    print(next(gen_obj))
    print(next(gen_obj))
    # print(next(gen_obj))