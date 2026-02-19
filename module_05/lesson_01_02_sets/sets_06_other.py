my_animals = {"Cat", "Dog"}
shop_animals = {"Cat", "Turtle", "Snake", "Dog"}
wild_animals = {"Fox", "Owl", "Snake"}

result = my_animals.issubset(shop_animals)
print(result)
result = shop_animals.issuperset(my_animals)
print(result)

result = my_animals.isdisjoint(wild_animals)
print(result)
result = shop_animals.isdisjoint(wild_animals)
print(result)


my_animals = {"Cat", "Dog", "Parrot"}
shop_animals = {"Cat", "Turtle", "Snake", "Dog"}
result = my_animals.symmetric_difference(shop_animals)
print(result)
