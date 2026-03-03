import os

current_dir = r'.'
new_dir_01 = r'new_dir_01'
new_dir_02 = r'new_dir_02'

path_new_dir_01 = os.path.join(current_dir, new_dir_01)
path_new_dir_02 = os.path.join(current_dir, new_dir_02)

# try:
#     os.mkdir(path_new_dir_01)
# except FileExistsError:
#     print(f'Невозможно создать файл, так как он уже существует')
# except IOError:
#     print(f'Нет доступа к данной функции')

os.makedirs(path_new_dir_02, exist_ok=True)

try:
    os.rmdir(path_new_dir_01)
except FileNotFoundError:
    print(f'Не удается найти указанную папку')

try:
    os.rmdir(path_new_dir_02)
except FileNotFoundError:
    print(f'Не удается найти указанную папку')
