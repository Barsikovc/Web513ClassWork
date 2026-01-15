while True:
    try:
        num = float(input("Введите число: "))
        start = int(input('Введите с какой степени возводить: '))
        end = int(input('Введите до какой степени возводить (включительно): '))
        if start > end:
            print('Начало диапазона степеней не может быть больше конца.')
            continue
    except ValueError as ve:
        print(f'!!{type(ve).__name__}!!', "Ошибка ввода число может быть или int или float.\nСтепени только int")
    else:
        for exp in range(start, end + 1):
            result = num ** exp
            print(f'{num} в степени {exp}, равно: {result}')
        break


# num = int(input("Введите число: "))
# start = int(input("Введите с какой степени возводить: "))
# end = int(input("Введите по какую степень возводить: "))
#
# for exp in range(start, end + 1):
#     result = num ** exp
#     print(f"{num} в степени {exp}, равно {result}")
# print()