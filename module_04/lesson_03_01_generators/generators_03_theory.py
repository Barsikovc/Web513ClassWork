import sys

numbers_list = [x ** 2 for x in range(1000)]
# print(numbers_list)
numbers_gen = (x ** 2 for x in range(1000))
# print(numbers_gen)

print(f'Размер списка: {sys.getsizeof(numbers_list)} байт.')
print(f'Размер генератора: {sys.getsizeof(numbers_gen)} байт.')
