import json


def get_data_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            python_data = json.load(file)
    except FileNotFoundError:
        print(f'Файл не найден')
        return None
    except json.JSONDecodeError:
        print(f'Ошибка декодирования файла')
        return None
    else:
        return python_data

def get_data_from_json_string(data):
    python_data = json.loads(data)
    return python_data


if __name__ == '__main__':
    my_filename = r'data_files\data.json'
    my_data = get_data_from_json(my_filename)
    print(my_data)
    json_string = '{"0": "Нулевой", "1": true, "2": false, "3": null, "4": ["data1", "data2"], "5": {"key1": "value1"}}'
    print(get_data_from_json_string(json_string))
    print(type(get_data_from_json_string(json_string)))
