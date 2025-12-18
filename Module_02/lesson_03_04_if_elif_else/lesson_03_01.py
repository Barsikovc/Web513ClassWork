print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
empty_set = set()
print(bool(empty_set))
print(bool(0))
print(bool(0.0))
print(bool(None))
print()

print(bool("Some data"))
print(bool(['item', 2, 2.5]))
print(bool(('item', 2, 2.5)))
print(bool({'item', 'item1', 'item2'}))
print(bool({'key_1': 'value_1', 'key_2': 'value_2'}))
print(bool(2))
print(bool(0.05))
print()

data = [
    {'key': 'value'}
]

if data:
    print(f'Обработка данных')
    print(data)
else:
    print(f'Сообщаем об ошибке/отсутствии данных')

if not data:
    print(f'Сообщаем об ошибке/отсутствии данных')
else:
    print(f'Обработка данных')
    print(data)
