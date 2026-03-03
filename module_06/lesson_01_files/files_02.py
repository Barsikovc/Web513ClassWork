import os

path_learning = '.'

print(os.path.isabs(path_learning))
print(os.path.isfile(path_learning))
print(os.path.isdir(path_learning))
print(os.path.islink(path_learning))
print()

path_learning = r'.\files_01.py'

print(os.path.isabs(path_learning))
print(os.path.isfile(path_learning))
print(os.path.isdir(path_learning))
print(os.path.islink(path_learning))
print()

path_learning = os.path.abspath('.')
print(os.path.isabs(path_learning))
print(os.path.isfile(path_learning))
print(os.path.isdir(path_learning))
print(os.path.islink(path_learning))
