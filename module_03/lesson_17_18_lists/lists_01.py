category_list = ['Drama', 'Comedy', 'Fantasy']
print(category_list)
print(type(category_list))

category_list_01 = list(('Drama', 'Comedy', 'Fantasy'))
print(category_list_01)
print(type(category_list_01))
print()

category_list_02 = []
category_list_03 = list()

print(category_list_02)
print(category_list_03)
print()

print(bool(category_list_01))
print(bool(category_list_02))

if category_list_01:
    print(f'Список не пустой')
else:
    print(f'Список пустой.')

if not category_list_02:
    print(f'Список пустой.')
else:
    print(f'Список не пустой')
