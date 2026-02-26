my_dict_01 = {}
print(type(my_dict_01))
print(my_dict_01)

my_dict_02 = dict()
print(my_dict_02)

employees_dict = {'Петр': 201, 'Мария': 201}
print(employees_dict)
some_dict = {'Петр': "Имя", 'Python': "Язык Программирования"}
print(some_dict)
dict_keys_num = {1: "Очень плохо", 2: "Плохо", 3: "Удовлетворительно"}
print(dict_keys_num)
print()

keyword_dict = dict(name="Петр", python='Язык программирования')
animals_dict = dict([('cat', 'кот'), ('dog', 'собака'), ('snake', 'змея')])
print(keyword_dict)
print(animals_dict)

explanations = {True: "Ответ верный", False: "Нет это неверно!"}
user_num = int(input('Введите целое число меньше 10: '))

# if user_num < 10:
#     print(explanations[True])
# else:
#     print(explanations[False])

print(explanations[user_num < 10])
print(explanations[user_num >= 10])
