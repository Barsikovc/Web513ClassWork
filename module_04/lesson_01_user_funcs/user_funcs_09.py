def calc_result(numbers: str):
    numbers_list = prepare_numbers(numbers)
    result_sum = 0
    for number in numbers_list:
        result_sum += int(number)
    return result_sum


def prepare_numbers(numbers: str):
    numbers_list = numbers.split()
    return numbers_list


def main():
    user_numbers = input('Введите числа через пробел: ')
    user_result = calc_result(user_numbers)
    print(f'Ващ результат: {user_result}')


if __name__ == '__main__':
    main()
