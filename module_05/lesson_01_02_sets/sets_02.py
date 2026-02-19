animals_set = {'Cat', 'Dog', 'Turtle'}
animals_set.add('Parrot')
animals_set.add('Owl')
print(animals_set)

popped_item = animals_set.pop()
print(popped_item)
print(animals_set)

discarded_item = 'Dog'
animals_set.discard(discarded_item)
print(animals_set)

removed_item = 'Owl'
if removed_item in animals_set:
    animals_set.remove(removed_item)
    print(animals_set)
else:
    print(f'Элемент: {removed_item} - не найден в множестве')
print()

for item in animals_set:
    print(item)
print()

animals_set.clear()
print(animals_set)
