def fib_gen(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


# def fib_gen1(limit):
#     i = 0
#     a, b = 0, 1
#     while i < limit:
#         yield a
#         a, b = b, a + b
#         i += 1


if __name__ == '__main__':
    for number in fib_gen(56):
        print(number)

    # for number in fib_gen1(11):
    #     print(number)
