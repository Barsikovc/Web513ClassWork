def get_total_check(prices, tip=0):
    check_sum = sum(prices)
    tip_sum = check_sum * tip / 100
    total_check = check_sum + tip_sum
    return total_check


if __name__ == '__main__':
    sum_list = [1000, 3000, 500]
    tip_percent = 10
    total_0 = get_total_check(sum_list)  # prices=sum_list
    total_10 = get_total_check(sum_list, tip_percent)  # prices=sum_list, tip=tip_percent
    print(f'Итого: {total_0}')
    print(f'Итого: {total_10}')
