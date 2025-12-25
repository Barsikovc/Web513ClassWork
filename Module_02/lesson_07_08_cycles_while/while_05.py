shopping_matrix = []

while True:
    user_input = input('Введите вашу покупку или стоп: ').strip().lower()
    user_sum = 0
    if user_input == 'стоп':
        break
    while True:
        try:
            user_sum = float(input(f'Введите сумму покупки {user_input}: '))
            break
        except ValueError:
            print(f'Ошибка ввода! Введите число!')

    shopping_matrix.append([user_input, user_sum])

# print(shopping_matrix)

"""
[
['кофе', 150.0], 
['булочка', 100.0], 
['печенье', 250.0]
]
"""

if shopping_matrix:
    while True:
        user_choice = input('Вывести только покупки - 1\nВывести только суммы - 2\nВывести все + итог - 3\nВыход - 0\nВаш выбор: ')
        if user_choice == '0':
            print(f'Программа завершена!')
            break
        elif user_choice == '1':
            print('Список покупок: ')
            for purchase, price in shopping_matrix:
                print(purchase)
        elif user_choice == '2':
            print(f'Список сумм: ')
            for purchase, price in shopping_matrix:
                print(price)
        elif user_choice == '3':
            total_sum = 0
            print('Покупки и суммы: ')
            for purchase, price in shopping_matrix:
                print(f'Покупка: {purchase}. Цена {price}')
                total_sum += price
            print(f'Итого покупок {len(shopping_matrix)} на сумму: {total_sum}')
        else:
            print('Ошибка ввода!')
else:
    print(f'Вы ничего не купили.')
