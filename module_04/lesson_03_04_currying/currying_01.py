def simple_greet(greeting, name):
    print(f'{greeting}, {name}!')


def greet_curried(greeting):
    def greet(name):
        print(f'{greeting}, {name}')

    return greet


if __name__ == '__main__':
    simple_greet('Привет', "Дмитрий")
    print()
    greet_hello = greet_curried('Привет')
    greet_hello('Дмитрий')
    greet_hello('Иван')
