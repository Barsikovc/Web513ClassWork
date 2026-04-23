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

    @classmethod
    def cat_to_json(cls, obj):
        if isinstance(obj, MyCat):
            result = obj.__dict__
            result['ClassName'] = obj.__class__.__name__
            result['methods'] = {
                'property_name': obj.name,
                'property_age': obj.age,
                'property_gender': obj.gender
            }
            return result
        raise TypeError('Объект неподходящего класса!')


if __name__ == '__main__':
    my_cat = MyCat('Франц', 4, 'Самец')
    json_data = json.dumps(my_cat, default=MyCat.cat_to_json, ensure_ascii=False)
    print(json_data)

    with open(r'json_files\my_cat_cls.json', 'w', encoding='utf-8') as fh:
        json.dump(my_cat, fh,
                  default=MyCat.cat_to_json,
                  ensure_ascii=False, indent=2)

    try:
        with open(r'json_files\my_cat_cls.json', 'r', encoding='utf-8') as fh:
            python_cat = json.load(fh)
    except FileNotFoundError:
        print('Файл не найден!')
    except JSONDecodeError:
        print(f'Ошибка декодирования файла!')
    except Exception as ex:
        print(f'Ошибка: {ex}')
    else:
        print(python_cat)
        my_cat_obj = MyCat(python_cat['_name'], python_cat['_age'], python_cat['_gender'])
        print(my_cat_obj)
        print(my_cat_obj.name)
