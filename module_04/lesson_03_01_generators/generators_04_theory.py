import sys

squares = (x ** 2 for x in range(1000))  # генератор мало памяти создание на ходу, по запросу.
print(next(squares))
print(next(squares))
print(next(squares))

# генераторные выражения, внутри себя работают как генератор, но возвращают уже готовые данные (полностью)
# занимают значительно больше памяти.
squares_dict = {f'{x}': x ** 2 for x in range(6)}
print(squares_dict)

squares_set = {x ** 2 for x in range(6)}
print(squares_set)

even_numbers = [x for x in range(11) if x % 2 == 0]
print(even_numbers)

odd_squares_dict = {x: x ** 2 for x in range(11) if x % 2 != 0}
print(odd_squares_dict)
