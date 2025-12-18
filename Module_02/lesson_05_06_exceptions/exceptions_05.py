try:
    raise Exception
except Exception:
    print('Хмм... Что-то пошло не так')
except ValueError as ve:
    print(f'Получено нужное исключение {type(ve).__name__}')

try:
    raise ValueError
except Exception:
    print('Хмм... Что-то пошло не так')
except ValueError as ve:
    print(f'Получено нужное исключение {type(ve).__name__}')

try:
    raise ValueError
except ValueError as ve:
    print(f'Получено нужное исключение {type(ve).__name__}')
except Exception:
    print('Хмм... Что-то пошло не так')

try:
    raise Exception
except ValueError as ve:
    print(f'Получено нужное исключение {type(ve).__name__}')
except Exception as ex:
    print(f'Хмм... Что-то пошло не так {type(ex).__name__}')
