import os
import shutil

my_path = r'dir_02/file1_new_place.txt'

try:
    os.remove(my_path)
except FileNotFoundError:
    print(f'Файл не найден')
else:
    print(f'Файл успешно удален')
print()

my_path = r'dir_02'
try:
    shutil.rmtree(my_path)
except FileNotFoundError:
    print(f'Файл не найден')
else:
    print(f'Файл успешно удален')
print()
