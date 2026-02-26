fruits = {
    'яблоки': 400,
    'груши': 200,
    'персики': 600,
}

user_fruit = input('Выберете фрукт: ')
fruit_weight = float(input('Введите вес в граммах: '))

if user_fruit in fruits:
    price = fruits[user_fruit] * fruit_weight / 1000
    print(f'Стоимость: {price} рублей')
else:
    print(f'{user_fruit} нет в ассортименте')
