# Блоки выполнения для:
# Условных конструкций
# data = [
#     {'key': 'value'}
# ]
#
# if data:
#     print(f'Обработка данных')
#     print(data)
# else:
#     print(f'Сообщаем об ошибке/отсутствии данных')
# print()
#
# # циклов
# counter = 0
# while counter < 5:
#     print("Inside cycle")
#     counter += 1
# print("Outside cycle\n")
#
# for i in range(5):
#     print(f"Inside cycle. i = {i}")
# print("Outside range cycle\n")
#
# some_list = ['item_1', 'item_2', 'item_3']
# for item in some_list:
#     print(item)
# print()

# исключения
try:
    print('Провокация')
except Exception:
    print("Обход исключение если провокация сработала")
else:
    print("Выполняется если исключений не было")
finally:
    print("Выполняем в любом случае")
print()


# функции
def some_func():
    print('Внутри функции')


some_func()
print()


class ExampleClass:

    def __init__(self, attr):
        self.attr = attr

    def display_attr(self):
        print(self.attr)


my_obj = ExampleClass('Some Attr')
my_obj.display_attr()