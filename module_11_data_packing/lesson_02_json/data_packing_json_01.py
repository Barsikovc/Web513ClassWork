import json

my_dict = {
    'my_string': 'some_string',
    'my_integer': 123,
    'my_tuple': (1, 2, 3, 4, 5),
    'my_bool': True,
    'my_none': None,
}

json_string = json.dumps(my_dict, ensure_ascii=False)
print(json_string)
print(type(json_string))
python_data = json.loads(json_string)
print(python_data)
print(type(python_data))
for key, value in python_data.items():
    if 'tuple' in key:
        python_data[key] = tuple(value)
print(python_data)
