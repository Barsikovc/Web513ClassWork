import json
from json import JSONDecodeError


class MyCat:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


if __name__ == '__main__':
    my_cat = MyCat('Франц', 4, 'Самец')
    # json_data = json.dumps(my_cat)
    print(my_cat.__dict__)
    json_data = json.dumps(my_cat, default=lambda my_cat_obj: my_cat_obj.__dict__, ensure_ascii=False)
    print(json_data)

    with open(r'json_files\my_cat.json', 'w', encoding='utf-8') as fh:
        json.dump(my_cat, fh,
                  default=lambda my_cat_obj: my_cat_obj.__dict__,
                  ensure_ascii=False, indent=2)

    try:
        with open(r'json_files\my_cat.json', 'r', encoding='utf-8') as fh:
            python_cat = json.load(fh)
    except FileNotFoundError:
        print('Файл не найден!')
    except JSONDecodeError:
        print(f'Ошибка декодирования файла!')
    except Exception as ex:
        print(f'Ошибка: {ex}')
    else:
        my_cat_obj = MyCat(**python_cat)
        print(my_cat_obj)
        print(my_cat_obj.name)

