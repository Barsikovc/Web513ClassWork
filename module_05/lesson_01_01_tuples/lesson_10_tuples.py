# Исходный кортеж с целыми числами
numbers = (1, 23, 456, 7, 89, 1234, 56789, -12, 0, 345)

# Словарь для хранения статистики
digit_count = {}


# Подсчет количества цифр в каждом числе
for number in numbers:
    # Берем абсолютное значение числа и преобразуем его в строку
    count_of_digits = len(str(abs(number)))

    # Обновляем статистику
    if count_of_digits in digit_count:
        digit_count[count_of_digits] += 1
    else:
        digit_count[count_of_digits] = 1

# Вывод результата
for digit, count in sorted(digit_count.items()):
    print(f'{digit} разряд(а/ов) - {count} элемент(ов)')