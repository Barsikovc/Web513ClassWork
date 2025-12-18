weather = input("Введите какая сегодня погода: 1 - хорошая/2 - плохая: ")
tickets = input("Есть ли билеты: 1 - да/2 - нет: ")
table = input('Есть ли столик: 1 - да/2 - нет: ')

if weather == '1':
    print(f'Идем гулять!')
elif tickets == '1':
    print('Идем в кино!')
elif table == '1':
    print(f'Идем в ресторан!')
else:
    print(f'Вечер пиццы и настолок!')

user_choice = input(
    "Введите какая сегодня погода:\n1 - для прогулок\n2 - для кино\n3 - для ресторана\n4 - для сиденья дома\nВаш выбор: ")

if user_choice == '1':
    print(f'Идем гулять!')
elif user_choice == '2':
    print('Идем в кино!')
elif user_choice == '3':
    print(f'Идем в ресторан!')
elif user_choice == '4':
    print(f'Вечер пиццы и настолок!')
else:
    print(f'Ошибка ввода! Перезапустите программу!')
