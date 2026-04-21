import pickle

data = {
    'nums': [1, 2, 3, 4, 5, 5 + 5],
    'strings': ['character_string', b'byte_string'],
    'other': [None, True, False]
}

# для обычной работы
my_data_s = pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)
print(my_data_s)
print(type(my_data_s))

my_data_ds = pickle.loads(my_data_s)
print(my_data_ds)
print(type(my_data_ds))

# для работы с файлами, для сохранения промежуточного состояния программы
with open('data_pickle.txt', 'wb') as file:
    pickle.dump(my_data_ds, file, protocol=5)

try:
    with open('data_pickle.txt', 'rb') as file:
        my_data_ff = pickle.load(file)
    print(my_data_ff)
except FileNotFoundError:
    print(f'Файл не найден')
except Exception as ex:
    print(ex)


