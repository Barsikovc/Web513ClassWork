def decorator(func):
    def wrapper():
        print('Инструкции до вызова функции')
        func()
        print('Инструкции после вызова функции')

    return wrapper


@decorator
def say_hello():
    print('Hello world!')


@decorator
def say_goodbye():
    print('Good bye!')


if __name__ == '__main__':
    say_hello()
    print()
    say_goodbye()
