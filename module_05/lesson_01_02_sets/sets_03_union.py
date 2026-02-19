my_animals = {'Cat', 'Dog'}
shop_animals = {'Cat', 'Turtle', 'Snake'}
wild_animals = {'Fox', 'Owl', 'Snake'}

all_animals_set_a = my_animals.union(shop_animals).union(wild_animals)
all_animals_set_b = my_animals | shop_animals | wild_animals
print(all_animals_set_a)
print(all_animals_set_b)
print()

my_animals = {'Cat', 'Dog'}
shop_animals = ['Cat', 'Turtle', 'Snake']
wild_animals = ('Fox', 'Owl', 'Snake')
all_animals_set = my_animals.union(shop_animals).union(wild_animals)
print(all_animals_set)

