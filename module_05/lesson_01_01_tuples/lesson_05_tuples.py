# animals_tuple = ("Cat", 'Turtle', 'Snake', 'Dog')
#
# animal_input = input('Введите животное: ')
# print(animal_input in animals_tuple)
#
# if animal_input in animals_tuple:
#     print(f'{animal_input} есть в кортеже {animals_tuple}')
# else:
#     print(f'{animal_input} нет в кортеже {animals_tuple}')


animals_tuple = ("Cat", 'Turtle', 'Snake', 'Dog')

for animal in animals_tuple:
    print(animal)
print()

for i in range(len(animals_tuple)):
    print(animals_tuple[i])
print()

for idx, item in enumerate(animals_tuple):
    print(f'{idx} >> {item}')