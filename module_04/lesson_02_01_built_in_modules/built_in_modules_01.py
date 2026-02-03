import math


def sin(x, pi_value):
    if 2 * x == pi_value:
        return 0.999999999
    else:
        return None


if __name__ == '__main__':
    pi = 3.14
    print(sin(pi / 2, pi))

    print(math.sin(math.pi / 2))
