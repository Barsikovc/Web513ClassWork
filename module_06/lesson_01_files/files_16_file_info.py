import os


my_path = r'data_files\shopping_list.txt'
print(os.path.getctime(my_path))
print(os.path.getmtime(my_path))
print(os.path.getatime(my_path))
print(os.path.getsize(my_path))



