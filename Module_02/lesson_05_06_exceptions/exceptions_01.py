from datetime import datetime

try:
    print('Код который может вызвать ошибку: ')
    num = int(input('Введите целое число: '))
    print(10 / num)
except ValueError:
    print(f'Введено неверное значение, допустимы только целые числа.')
except ZeroDivisionError:
    print('Попытка деления на 0')
except Exception as ex:
    print('Код на случай неизвестного исключение.')
    print(type(ex).__name__)
    with open('logging.log', 'a', encoding='utf-8') as file:
        file.write(f'{datetime.now().strftime('%d-%m-%Y - %H:%M:%S')} >>> {type(ex).__name__}\n')
else:
    print('Код который будет выполнен если не было никаких исключений')
    print(num * 2)
finally:
    print(f'Код который выполнится в любом случае.')
