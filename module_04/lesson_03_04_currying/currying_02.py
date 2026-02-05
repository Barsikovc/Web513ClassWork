def greet_deeply_curried(greeting):
    def w_separator(separator):
        def w_emphasis(emphasis):
            def w_name(name):
                print(greeting + separator + name + emphasis)

            return w_name

        return w_emphasis

    return w_separator


if __name__ == '__main__':
    greet = greet_deeply_curried('Привет')('/.../')('!!!')
    greet('Дмитрий')
    greet('Петр')
