# print(sum([1, 2, 3], 4))

def new_sum(*args, start_value=0):
    # print(args)
    # print(type(args))
    args_list = list(args)
    total_sum = start_value
    for num in args_list:
        if type(num) is int or type(num) is float:
            total_sum += num
        else:
            print(f'В данных есть объекты не относящиеся к числам: {num}')
    return total_sum


if __name__ == '__main__':
    print(new_sum(1, 2, 3, 4, 5, 'a', start_value=10))
