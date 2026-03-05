import json


def write_data_to_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f'Данные записаны успешно!')


def make_json_string(data):
    json_string = json.dumps(data, ensure_ascii=False, indent=4)
    return json_string


if __name__ == '__main__':
    my_filename = r'data_files\data.json'
    my_data = {
        0: 'Нулевой',
        1: True,
        2: False,
        3: None,
        4: ('data1', 'data2'),
        5: {'key1': 'value1'}
    }
    write_data_to_json(my_filename, my_data)
    print(make_json_string(my_data))
    print(type(make_json_string(my_data)))
