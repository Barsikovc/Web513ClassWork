# animals_dict = {'cat': 'котейка', 'dog': 'собачка'}
# print(animals_dict['cat'], animals_dict['dog'])
#
# animals_dict['owl'] = 'совушка'
# print(animals_dict)
#
# animals_dict['cat'] = 'кот'
# animals_dict['dog'] = 'собака'
# animals_dict['owl'] = 'сова'
# print(animals_dict)
#
# del animals_dict['owl']
# print(animals_dict)

animals_dict = {'cat': 'кот', 'dog': 'собака'}
animals_dict['der Kater'] = animals_dict['cat']
del animals_dict['cat']
print(animals_dict)

# popped_value = animals_dict.pop('dog')
# print(popped_value)

animals_dict['der Hund'] = animals_dict.pop('dog')
print(animals_dict)
