try:
    amount = int(input("Введите количество полученных предметов: "))
    items_type = input("Укажите тип полученных предметов (ящик или коробка): ")
    parts_quantity = int(input("Введите количество частей на которую будет разбита вся партия: "))
    amount_1_part = amount // parts_quantity
    amount_1_part_rest = amount % parts_quantity
except ValueError:
    print(f'Количество предметов/частей должно быть целым числом.')
except ZeroDivisionError:
    print('Невозможно разбить партию на 0 частей')
except Exception as ex:
    print(type(ex).__name__)
    print(repr(ex))
else:
    print(f'Партия из {amount} предметов. Тип: {items_type}. Успешно добавлена на склад')
    print(f'Каждая из {parts_quantity} частей состоит из {amount_1_part} указанных предметов.')
    if amount_1_part_rest != 0:
        print(f'Нераспределенный остаток: {amount_1_part_rest} указанных предметов.')
finally:
    print('Программа завершила свою работу.')
