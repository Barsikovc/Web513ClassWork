def calc_result(numbers: list[str]):
    result_sum = 0
    for number in numbers:
        result_sum += int(number)
    return result_sum


def prepare_numbers(numbers: str):
    numbers_list = numbers.split()
    return numbers_list


def main():
    user_numbers = input('Введите числа через пробел: ')
    user_numbers_list = prepare_numbers(user_numbers)
    user_result = calc_result(user_numbers_list)
    print(f'Ващ результат: {user_result}')


if __name__ == '__main__':
    main()
