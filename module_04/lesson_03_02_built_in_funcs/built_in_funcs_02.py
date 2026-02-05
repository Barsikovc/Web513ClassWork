def printfunction(fun, *args):
    for x in args:
        print(f'f({x}) = {fun(x)}', sep=', ')


def poly(x):
    return 2 * x ** 2 - 4 * x + 2


if __name__ == '__main__':
    printfunction(poly, *[x for x in range(-2, 3)])  # printfunction(poly, -2, -1, 0, 1, 2)
    print()
    printfunction(lambda x: 2 * x ** 2 - 4 * x + 2, *[x for x in range(-2, 3)])
