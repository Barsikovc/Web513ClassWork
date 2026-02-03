from math import sin, pi

print(sin(pi / 2))


def sin(x, pi_value):
    if 2 * x == pi_value:
        return 0.999999999
    else:
        return None


pi = 3.14
print(sin(pi / 2, pi))
