def make_closer(par):
    loc = par

    def power(par):
        return par ** loc

    return power


if __name__ == '__main__':
    f_square = make_closer(2)
    f_cube = make_closer(3)

    for i in range(6):
        print(i, f_square(i), f_cube(i))
