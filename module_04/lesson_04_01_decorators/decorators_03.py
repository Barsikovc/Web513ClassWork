def decorator(func):
    def wrapper(name):
        print('Инструкции до вызова функции')
        func(name)
        print('Инструкции после вызова функции')

    return wrapper


@decorator
def say_greet_name(name):
    print(f'Hello {name}!')


@decorator
def say_goodbye(name):
    print(f'Good bye {name}!')


if __name__ == '__main__':
    say_greet_name('Ivan')
    print()
    say_goodbye('Ivan')
