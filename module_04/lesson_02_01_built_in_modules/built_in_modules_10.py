from math import ceil, floor, trunc, factorial

x = 3.4
y = 5.6

print(f'Верхнее округление', ceil(x), ceil(y))
print(f'Верхнее округление', ceil(-x), ceil(-y))
print(f'Нижнее округление', floor(x), floor(y))
print(f'Нижнее округление', floor(-x), floor(-y))

print('Усечение до целого числа', trunc(x), trunc(y))
print('Усечение до целого числа', trunc(-x), trunc(-y))

print(f'Факториал', factorial(5))
