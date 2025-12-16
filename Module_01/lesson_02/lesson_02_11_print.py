def display_text():
    print('Какой-то текст')


def get_sum(a, b):
    return a + b


display_text()
result = get_sum(3, 2)
print(result)
print(get_sum(3, 4))  # == print(7)

print('Hello', 'World', 3, 3.5, sep=' & ', end='\n\t')
print('Hello', 'World', 3, 3.5, sep=' & ')

