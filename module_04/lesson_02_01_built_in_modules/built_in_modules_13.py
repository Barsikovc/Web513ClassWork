from random import shuffle, sample, choice, choices

some_list = [1, 2, 3, 5, 6, 7]
print(f'Список до перемешивания: {some_list}')
shuffle(some_list)
print(f'Перемешанный список: {some_list}')

random_values_from_list = sample(some_list, 3)
print(random_values_from_list)

print(f'Случайное значение из списка: {choice(some_list)}')
print(f'Случайные значения из списка: {choices(some_list, k=3)}')


