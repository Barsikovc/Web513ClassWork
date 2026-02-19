animals_tuple = ('Cat', 'Turtle', 'Snake')
animals_list = list(animals_tuple)
animals_list[2] = 'Python'
animals_list.append('Dog')
animals_list.remove('Turtle')
animals_tuple1 = tuple(animals_list)
print(animals_tuple1)

animals_tuple = ('Cat', 'Turtle', 'Snake', 'Dog')
animals_tuple = animals_tuple[0:2] + ('Python',) + animals_tuple[3:] + ('Owl', 'Dog')
print(animals_tuple)

print(animals_tuple.index('Turtle'))
print(animals_tuple.count('Dog'))