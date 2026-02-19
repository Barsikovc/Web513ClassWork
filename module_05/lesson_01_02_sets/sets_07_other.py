shop_animals = {"Cat", "Turtle", "Snake", "Parrot"}
wild_animals = {"Fox", "Owl", "Snake", "Turtle"}

shop_animals.update(wild_animals)  # union and update
print(shop_animals)

shop_animals = {"Cat", "Turtle", "Snake", "Parrot"}
wild_animals = {"Fox", "Owl", "Snake", "Turtle"}
shop_animals.intersection_update(wild_animals)
print(shop_animals)

shop_animals = {"Cat", "Turtle", "Snake", "Parrot"}
wild_animals = {"Fox", "Owl", "Snake", "Turtle"}
shop_animals.difference_update(wild_animals)
print(shop_animals)

shop_animals = {"Cat", "Turtle", "Snake", "Parrot"}
wild_animals = {"Fox", "Owl", "Snake", "Turtle"}
shop_animals.symmetric_difference_update(wild_animals)
print(shop_animals)