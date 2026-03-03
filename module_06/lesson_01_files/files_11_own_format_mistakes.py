def get_shopping_data(filename):
    items_count = 0
    items_sum = 0
    row_number = 0
    try:
        with open(filename, encoding='utf-8') as file:
            for item_data in file:
                row_number += 1
                # if item_data.count(' || ') < 2:
                #     print(f'Ошибка в строке {row_number} >> {item_data.strip()}')
                #     continue
                temp_data = item_data.strip().split(' || ')
                if len(temp_data) != 3:
                    print(f'Ошибка в строке {row_number} >> {item_data.strip()}')
                    continue
                item, quantity, price = temp_data
                print(item, quantity, price)
                items_sum += float(quantity) * float(price)
                items_count += 1
    except FileNotFoundError:
        print(f'Файл: {filename} не найден')
        return None, None
    except ValueError:
        print(f'Ошибка в значении веса/цены')
        return None, None
    return items_count, items_sum


if __name__ == '__main__':
    my_file = r'data_files/shopping_list.txt'
    try:
        my_count, my_sum = get_shopping_data(my_file)
        print(f'В списке {my_count} позиций, общая сумма: {my_sum} рублей')
    except Exception as e:
        print(e)
