# file = open(r'data_files\file_for_reading.txt', 'rt', encoding='utf-8')
# content = file.read()
# file.close()
# print(content)
# print()

# try:
#     with open(r'data_files\file_for_reading.txt', 'rt', encoding='utf-8') as file:
#         content = file.read()
# except FileNotFoundError as err:
#     print(err)
# else:
#     print(content)
# print()

def get_data_from_file(file_path):
    with open(file_path, 'rt', encoding='utf-8') as file:
        content = file.read()
    return content


if __name__ == '__main__':
    my_filepath = r'data_files\file_for_reading.txt'
    data = None
    try:
        data = get_data_from_file(my_filepath)
    except FileNotFoundError as err:
        print(err)

    if data:
        print(data)
    else:
        print(f'Данные не были получены')
