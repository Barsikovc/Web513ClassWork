# def get_order_total_sum(order_total, country):
#     total = 0
#     for items_price_quant in order_total.values():
#         total += items_price_quant[0] * items_price_quant[1]
#
#     if country == "RU":
#         total += total * 0.20  # RU НДС
#         return f'Общая сумма заказа RU: {total}'
#     elif country == 'KZ':
#         total += total * 0.16  # KZ ҚҚС
#         return f'Общая сумма заказа KZ: {total}'
#     else:
#         print(f'Не знаю такой страны')
#         return None
#
#
# if __name__ == '__main__':
#     order_1 = {
#         "Тормозные колодки": [100, 10],
#         "Диск сцепления": [250, 4],
#         "Фильтр масляный": [20, 50]
#     }
#     print(get_order_total_sum(order_1, 'RU'))
#     print(get_order_total_sum(order_1, 'KZ'))
#     print(get_order_total_sum(order_1, 'UAE'))


def get_order_total_sum(country_dict, order_total, country):
    total = 0
    for items_price_quant in order_total.values():
        total += items_price_quant[0] * items_price_quant[1]

    tax = get_tax_amount(country_dict, country)
    if tax:
        total += total * tax
        return f'Общая сумма заказа: {total}'
    print(f'Не знаю такой страны')
    return None


def get_tax_amount(country_dict, country):
    if country in country_dict:
        return country_dict[country]
    return None


# модуль (отдельно) интерфейса
def add_new_country(country_dict, country_code, tax):
    tax = tax / 100
    country_dict[country_code] = tax
    return country_dict


if __name__ == '__main__':
    country_taxes = {
        'RU': 0.2,
        'KZ': 0.16,
        'UAE': 0.05,
        'BY': 0.2
    }
    country_code = input('Введите код страны: ')
    country_tax = float(input('Введите ставку НДС: '))
    country_taxes_new = add_new_country(country_taxes, country_code, country_tax)

    order = {
        "Тормозные колодки": [100, 10],
        "Диск сцепления": [250, 4],
        "Фильтр масляный": [20, 50]
    }
    print(get_order_total_sum(country_taxes, order, 'RU'))
    print(get_order_total_sum(country_taxes, order, 'KZ'))
    print(get_order_total_sum(country_taxes, order, 'UAE'))
    print(get_order_total_sum(country_taxes, order, 'BY'))
    print(get_order_total_sum(country_taxes, order, 'AZ'))

