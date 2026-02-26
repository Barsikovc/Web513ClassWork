def calculate_price(fruits_dict, fruit, weight):
    if fruit in fruits_dict:
        price = fruits[user_fruit] * fruit_weight / 1000
        return price
    return None


if __name__ == '__main__':
    fruits = {
        'яблоки': 400,
        'груши': 200,
        'персики': 600,
    }

    user_fruit = input('Выберете фрукт: ')
    fruit_weight = float(input('Введите вес в граммах: '))
    result = calculate_price(fruits, user_fruit, fruit_weight)
    if not result:
        print(f'{user_fruit} нет в ассортименте')
    else:
        print(f'Стоимость: {result} рублей')
