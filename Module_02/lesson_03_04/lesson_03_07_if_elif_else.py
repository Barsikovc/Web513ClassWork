weather = input("Введите какая сегодня погода: 1 - хорошая/2 - плохая: ")

if weather == '1':
    print('Идем гулять')
else:
    tickets = input("Есть ли билеты: 1 - да/2 - нет: ")
    if tickets == '1':
        print('Пойдем в кино')
    else:
        table = input('Есть ли столик: 1 - да/2 - нет: ')
        if table == '1':
            print('Идем в ресторан')
        else:
            print(f'Вечер пиццы и настолок!')
