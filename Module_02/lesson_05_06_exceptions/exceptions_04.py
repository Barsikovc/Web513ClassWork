class OnlyPositiveException(Exception):
    def __init__(self, *args, **kwargs):
        pass


class PartsQuantityException(Exception):
    def __init__(self, *args, **kwargs):
        pass


class ItemTypeException(Exception):
    def __init__(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    try:
        apples = int(input('Введите количество яблок которое у вас есть: '))
        if apples <= 0:
            raise OnlyPositiveException()
    except ValueError:
        print("Количество должно быть целым числом")
    except OnlyPositiveException:
        print(f'У вас должно быть положительное количество яблок')
    else:
        print(f'У вас {apples} яблок')
