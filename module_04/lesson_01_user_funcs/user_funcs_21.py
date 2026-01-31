def calculate_way(v, t):
    way = v * t
    return way


if __name__ == '__main__':
    data_dict1 = {'v': 60, 't': 3}
    data_dict2 = {'v': 50, 't': 3}
    data_dict3 = {'v': 100, 't': 3}
    dicts_list = [data_dict1, data_dict2, data_dict3]
    for row, data_dict in enumerate(dicts_list):
        print(f'Matrix row {row + 1} distance: {calculate_way(**data_dict)}')
