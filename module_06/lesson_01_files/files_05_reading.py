def display_data_from_file(file_path):
    with open(file_path, 'rt', encoding='utf-8') as file:
        for line in file:
            print(line.rstrip())


def get_data_from_file(file_path: str) -> list[str]:
    content = []
    with open(file_path, 'rt', encoding='utf-8') as file:
        for line in file:
            content.append(line.rstrip())
    return content


def get_data_from_file_rl(file_path: str) -> list[str]:
    with open(file_path, 'rt', encoding='utf-8') as file:
        content = file.readlines()
    return content


if __name__ == '__main__':
    my_filepath = r'data_files\file_for_reading.txt'
    # display_data_from_file(my_filepath)
    print(get_data_from_file(my_filepath))
    print(get_data_from_file_rl(my_filepath))
