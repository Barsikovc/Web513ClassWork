from functools import reduce


def calculate_total_prices(prices, quantity, base_value=0):
    cart = list(zip(prices, quantity))  # собираем цени и количество в список кортежей

    # применяем lambda x к списку кортежей, map каждый раз берет кортеж из списка,
    # элементы кортежа извлекаются по индексам -> возвращается список значений итого по каждой позиции
    item_totals = map(lambda x: x[0] * x[1], cart)

    # складываем итоговые значения
    return reduce(lambda x, y: x + y, item_totals, base_value)


if __name__ == '__main__':
    my_prices = [10.99, 5.55, 8.99]
    my_quantity = [5, 3, 4]
    print(calculate_total_prices(my_prices, my_quantity))
    print()
    print(calculate_total_prices(my_prices, my_quantity, 20))
