even_numbers = 0
odd_numbers = 0

number = int(input(f'Введите целое число или 0 для остановки программы: '))

while number != 0:
    if number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1

    try:
        number = int(input(f'Введите целое число или 0 для остановки программы: '))
    except ValueError:
        print(f'Ошибка! Можно вводить только целые числа!')
        break
else:
    print('Цикл был завершен без прерываний')

print(f'Количество четных: {even_numbers}')
print(f'Количество нечетных: {odd_numbers}')
