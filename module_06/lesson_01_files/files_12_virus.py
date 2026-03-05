# virus_code = 'print("Я вирус")'
# with open('files_09_own_format_read.py', 'a', encoding='utf-8') as file:
#     file.write(f'\n{virus_code}\n')

# virus_code = 'print("Я вирус")'

def search_and_heal_file(filename, virus_pattern):
    with open(filename, encoding='utf-8') as file:
        content = file.read()
        if virus_pattern in content:
            print(f'Вирус обнаружен!!!')
            clean_content = content.replace(virus_pattern, '')
        else:
            print(f'Вирусов нет!')
    if clean_content:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(clean_content)
            print(f'Файл вылечен')


if __name__ == '__main__':
    virus_code = 'print("Я вирус")'
    search_and_heal_file('files_09_own_format_read.py', virus_code)
