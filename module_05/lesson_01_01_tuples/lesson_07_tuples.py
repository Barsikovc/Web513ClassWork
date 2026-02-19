animals_tuple = ("Cat", 'Turtle', 'Snake', 'Dog')
print(len(animals_tuple))

nums_tuple = (1, 2, 3, 4, 5)
print(sum(nums_tuple))

print(min(animals_tuple))
print(max(animals_tuple))

print(min(nums_tuple))
print(max(nums_tuple))

sorted_animals_tuple = tuple(sorted(animals_tuple))
print(sorted_animals_tuple)
sorted_animals_tuple_rev = tuple(sorted(animals_tuple, reverse=True))
print(sorted_animals_tuple_rev)

sorted_nums_tuple = tuple(sorted(nums_tuple))
print(sorted_nums_tuple)
sorted_nums_tuple_rev = tuple(sorted(nums_tuple, reverse=True))
print(sorted_nums_tuple_rev)

