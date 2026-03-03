def guests_manager(file_path):
    guests_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        guests_list = file.readlines()
    return len(guests_list), guests_list


if __name__ == '__main__':
    guests_data = r'data_files\guests.txt'
    try:
        guests_count, guests = guests_manager(guests_data)
    except FileNotFoundError:
        print(f'Список гостей не найден у указанном месторасположении >> {guests_data}')
    else:
        print(f'Всего гостей: {guests_count}')
        print(f'Список гостей:\n{''.join(guests)}')