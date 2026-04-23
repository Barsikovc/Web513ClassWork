import json
from json import JSONDecodeError

my_dict = {
    'my_string': 'some_string',
    'my_integer': 123,
    'my_tuple': (1, 2, 3, 4, 5),
    'my_bool': True,
    'my_none': None,
}

# with open(r'json_files\my_data.json', 'w', encoding='utf-8') as fh:
#     json.dump(my_dict, fh, ensure_ascii=False, indent=2)

try:
    with open(r'json_files\my_data.json', 'r', encoding='utf-8') as fh:
        python_data = json.load(fh)
except FileNotFoundError:
    print('Файл не найден!')
except JSONDecodeError:
    print(f'Ошибка декодирования файла!')
except Exception as ex:
    print(f'Ошибка: {ex}')
else:
    print(python_data)
