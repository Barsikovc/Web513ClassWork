import json
from json import JSONDecodeError


class MyCat:

    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender


class MyCatEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, MyCat):
            return {
                'name': o.name,
                'age': o.age,
                'gender': o.gender,
                'ClassName': o.__class__.__name__,
                'methods': {
                    'property_name': o.name,
                    'property_age': o.age,
                    'property_gender': o.gender
                }
            }
        raise TypeError('Объект неподходящего класса!')


if __name__ == '__main__':
    my_cat = MyCat('Франц', 4, 'Самец')
    json_data = json.dumps(my_cat, cls=MyCatEncoder, ensure_ascii=False)
    print(json_data)
    python_data = json.loads(json_data)
    print(python_data)

    with open(r'json_files\my_cat_encoder.json', 'w', encoding='utf-8') as fh:
        json.dump(my_cat, fh,
                  cls=MyCatEncoder,
                  ensure_ascii=False, indent=2)

    try:
        with open(r'json_files\my_cat_encoder.json', 'r', encoding='utf-8') as fh:
            python_cat = json.load(fh)
    except FileNotFoundError:
        print('Файл не найден!')
    except JSONDecodeError:
        print(f'Ошибка декодирования файла!')
    except Exception as ex:
        print(f'Ошибка: {ex}')
    else:
        print(python_cat)
        my_cat_obj = MyCat(python_cat['name'], python_cat['age'], python_cat['gender'])
        print(my_cat_obj)
        print(my_cat_obj.name)
