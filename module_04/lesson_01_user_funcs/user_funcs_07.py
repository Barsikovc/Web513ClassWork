a = 3
print(f'Global a: {a}')


def my_func():
    a = 4
    print(f'Local a: {a}')


my_func()
print(f'Global a: {a}')
print()

c = 30
print(f'Global c: {c}')


def my_func1():
    print(f'Local c: {c}')


my_func1()
print(f'Global c: {c}')
