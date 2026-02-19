my_animals = {'Cat', 'Dog'}
shop_animals = {'Cat', 'Turtle', 'Snake'}

only_my_animals = my_animals.difference(shop_animals)
print(only_my_animals)
only_shop_animals = shop_animals.difference(my_animals)
print(only_shop_animals)

only_my_animals_1 = my_animals - shop_animals
print(only_my_animals_1)
