def decorator1(func):
    def wrapper(name):
        print(f'Декоратор1 start')
        func(name)
        print(f'Декоратор1 end')

    return wrapper


def decorator2(func):
    def wrapper(name):
        print(f'Декоратор2 start')
        func(name)
        print(f'Декоратор2 end')

    return wrapper


@decorator1  # бант
@decorator2  # упаковочная бумага
def say_greet_name(name):
    print(f'Hello {name}')


if __name__ == '__main__':
    say_greet_name('Ivan')
