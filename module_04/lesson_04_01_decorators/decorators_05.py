def log_func(func):
    def wrapper(*args, **kwargs):
        print(f'Вызов функции {func.__name__} c аргументами {args} и {kwargs}')
        return func(*args, **kwargs)

    return wrapper
@log_func
def greet_deeply_curried(greeting):
    @log_func
    def w_separator(separator):
        @log_func
        def w_emphasis(emphasis):
            @log_func
            def w_name(name):
                print(greeting + separator + name + emphasis)

            return w_name

        return w_emphasis

    return w_separator


if __name__ == '__main__':
    greet = greet_deeply_curried('Привет')('/.../')('!!!')
    print()
    greet('Дмитрий')
    greet('Петр')
