from exceptions_04 import OnlyPositiveException, PartsQuantityException, ItemTypeException

try:
    amount = int(input("Введите количество полученных предметов: ").strip())
    if amount <= 0:
        raise OnlyPositiveException("Количество предметов должно быть положительным!!!")
    items_type = input("Укажите тип полученных предметов (ящик или коробка): ").strip().lower()
    if items_type != 'ящик' and items_type != 'коробка':
        raise ItemTypeException('Склад может принимать только ящики или коробки!!!')
    parts_quantity = int(input("Введите количество частей на которую будет разбита вся партия: "))
    if parts_quantity > amount:
        raise PartsQuantityException('Количество частей не может превышать количество предметов!!!')
    amount_1_part = amount // parts_quantity
    amount_1_part_rest = amount % parts_quantity
except ValueError:
    print(f'Количество предметов/частей должно быть целым числом.')
except ZeroDivisionError:
    print('Невозможно разбить партию на 0 частей')
except OnlyPositiveException as OPEx:
    print(OPEx)
except ItemTypeException as ITEx:
    print(ITEx)
except PartsQuantityException as PQEx:
    print(PQEx)
except Exception as ex:
    print(type(ex).__name__)
    print(repr(ex))
except:
    print("\nЧто то пошло не так!")
else:
    print(f'Партия из {amount} предметов. Тип: {items_type}. Успешно добавлена на склад')
    print(f'Каждая из {parts_quantity} частей состоит из {amount_1_part} указанных предметов.')
    if amount_1_part_rest != 0:
        print(f'Нераспределенный остаток: {amount_1_part_rest} указанных предметов.')
finally:
    print('Программа завершила свою работу.')
