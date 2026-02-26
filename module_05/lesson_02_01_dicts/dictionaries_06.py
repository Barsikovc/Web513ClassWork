# animals_dict = {'cat': 'Кошка', 'dog': 'Собака', 'bird': 'Птица'}
# animals_keys = animals_dict.keys()
# animals_values = animals_dict.values()
# animals_items = animals_dict.items()
#
# print(animals_dict)
# print(type(animals_keys), animals_keys)
# print(type(animals_values), animals_values)
# print(type(animals_items), animals_items)
#
# keys_list = list(animals_keys)
# values_list = list(animals_values)
# items_list = list(animals_items)
# print(keys_list, values_list, items_list)
#
# keys_list = [key for key in animals_dict.keys()]
# values_list = [value for value in animals_dict.values()]
# items_list = [(key, value) for key, value in animals_dict.items()]
# print(keys_list, values_list, items_list)

animals_dict = {'cat': 'Кошка', 'dog': 'Собака', 'bird': 'Птица'}
for animal in animals_dict:
    print(f"Это ключ - {animal}")
print()

for animal in animals_dict.keys():
    print(f"Это ключ - {animal}")
print()

for animal in animals_dict.values():
    print(f"Это значение - {animal}")
print()

for word, translate in animals_dict.items():
    print(f'Это ключ - {word}', end=' // ')
    print(f"Это значение - {translate}")
print()


dict_keys = []
dict_values = []
dict_items = []

for key, value in animals_dict.items():
    print(f"Это ключ - {key}")
    print(f"Это значение - {value}")
    dict_keys.append(key)
    dict_values.append(value)
    dict_items.append((key, value))

print(dict_keys)
print(dict_values)
print(dict_items)