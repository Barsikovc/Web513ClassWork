import os

# current_path = r'D:\work_Top_Academy_web\Web513ClassWork\module_06\lesson_01_files'
#
# # for path, dirnames, filenames in os.walk(current_path):
# #     print(f'path >> {path}')
# #     print(f'dirs >> {dirnames}')
# #     print(f'files >> {filenames}')
# #     print()
#
# disk = 'D:\\'
# dir1 = 'work_Top_Academy_web'
# dir2 = 'Web513ClassWork'
# dir3 = 'module_06'
# dir4 = 'lesson_01_files'
#
# path_m06_l01 = os.path.join(disk, dir1, dir2, dir3, dir4)
# print(path_m06_l01)
#
#
# for path, dirnames, filenames in os.walk(path_m06_l01):
#     print(f'path >> {path}')
#     print(f'dirs >> {dirnames}')
#     print(f'files >> {filenames}')
#     print()

base_dir = '.'
data_dir = 'dir_01'
print(os.path.join(base_dir, data_dir))
for path, dirnames, filenames in os.walk(os.path.join(base_dir, data_dir)):
    print(f'path >> {path}')
    print(f'dirs >> {dirnames}')
    print(f'files >> {filenames}')
    print()


print(os.path.abspath('.'))
print(os.path.abspath('files_01.py'))
print(os.path.abspath(r'dir_01\file1.txt'))
