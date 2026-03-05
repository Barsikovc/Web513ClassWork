import os

base_path = 'dir_01/file1.txt'
new_path = 'dir_02/file1_new_place.txt'

try:
    os.rename(base_path, new_path)
except FileNotFoundError:
    print(f'Файл не найден')
except FileExistsError:
    print(f'Такой файл уже существует!')
else:
    print(f'Файл успешно перемещен/переименован:\n{os.path.abspath(new_path)}')
print()

# renames умеет создавать директории если это необходимо,
# а также удаляет пустую директорию (из которой перемещали файл)
base_path = r'dir_01\file3.txt'
new_path = r'dir_03\file_03_new_place.txt'

try:
    os.renames(base_path, new_path)
except FileNotFoundError:
    print(f'Файл не найден')
except FileExistsError:
    print(f'Такой файл уже существует!')
else:
    print(f'Файл успешно перемещен/переименован:\n{os.path.abspath(new_path)}')
