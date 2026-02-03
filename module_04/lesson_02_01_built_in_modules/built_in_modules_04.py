from math import sin as m_sin, pi as m_pi


def sin(x, pi_value):
    if 2 * x == pi_value:
        return 0.999999999
    else:
        return None


pi = 3.14
print(sin(pi / 2, pi))

print(m_sin(m_pi / 2))
