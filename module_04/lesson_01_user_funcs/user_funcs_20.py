def calculate_way(v, t):
    way = v * t
    return way


if __name__ == '__main__':
    data_list1 = [60, 2]
    data_list2 = [40, 2]
    data_list3 = [100, 2]
    data_matrix = [data_list1, data_list2, data_list3]
    data_tuple = (50, 3)
    print(f'List distance: {calculate_way(*data_list1)}')  # v = 60, t = 2
    print(f'Tuple distance: {calculate_way(*data_tuple)}')  # v = 60, t = 2

    for row, data in enumerate(data_matrix):
        print(f'Matrix row {row + 1} distance: {calculate_vay(*data)}')
