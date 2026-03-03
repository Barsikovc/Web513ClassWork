with open(r'data_files\file_for_writing.txt', 'wt', encoding='utf-8') as file:
    file.write('Hello ')
    file.write('World\n')
    file.write('Привет ')
    file.write('Мир\n')


with open(r'data_files\file_for_writing.txt', 'at', encoding='utf-8') as file:
    file.write('\n')
    file.write('Hello ')
    file.write('World\n')
    file.write('Привет ')
    file.write('Мир\n')
