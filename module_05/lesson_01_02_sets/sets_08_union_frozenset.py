my_animals = frozenset(['Cat', 'Dog'])
shop_animals = frozenset({'Cat', 'Turtle', 'Snake'})
wild_animals = frozenset(('Fox', 'Owl', 'Snake'))
print(my_animals)

all_animals_set_a = my_animals.union(shop_animals).union(wild_animals)
all_animals_set_b = my_animals | shop_animals | wild_animals
print(all_animals_set_a)
print(all_animals_set_b)
