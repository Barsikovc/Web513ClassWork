my_list_01 = [i for i in range(1, 11)]
print(my_list_01)

my_list_02 = [i * i for i in range(1, 11)]
print(my_list_02)

my_list_02_simple = []
for i in range(1, 11):
    my_list_02_simple.append(i * i)
print(my_list_02_simple)

list_from_str = [sym + '*' for sym in 'my_string']
print(list_from_str)

list_from_str_simple = []
for sym in 'my_string':
    list_from_str_simple.append(sym + '*')
print(list_from_str_simple)
print()
