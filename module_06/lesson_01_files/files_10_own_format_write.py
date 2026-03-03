def write_managers_data_own_format(filename, data, divider):
    with open(filename, 'w', encoding='utf-8') as file:
        for (company, head_company), manager in data.items():
            file.write(f'{manager}{divider}{company}{divider}{head_company}\n')
    print(f'Данные успешно записаны')


if __name__ == '__main__':
    managers_to_write = {
        ('Bethesda', 'Microsoft'): 'Тодд Говард',
        ('ID Software', 'Microsoft'): 'Джон Кармак',
        ('AMD', 'AMD'): 'Лиза Су'
    }
    file_name = input('Введите имя файла сохранения: ')
    user_divider = input('Введите разделитель: ')
    file_name = fr'data_files\{file_name}.txt'
    write_managers_data_own_format(file_name, managers_to_write, user_divider)
