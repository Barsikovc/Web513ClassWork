my_list = [x for x in range(1, 6)]
map_obj = map(lambda x: 2 ** x, my_list)
print(map_obj)
degrees_list_from_map = list(map_obj)
print(degrees_list_from_map)

for x in map(lambda x: 2 ** x, my_list):
    print(x, end=' ')
print()


def my_func(x):
    return 2 ** x


for x in map(my_func, my_list):
    print(x, end=' ')
