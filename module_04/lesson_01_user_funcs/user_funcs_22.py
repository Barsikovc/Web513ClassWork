def calculate_way(v_l, t_l, v_d, t_d):
    way_l = v_l * t_l
    way_d = v_d * t_d
    return f'List distance: {way_l}\nDictionary distance: {way_d}'


if __name__ == '__main__':
    data_list1 = [60, 2]
    data_list2 = [40, 2]
    data_list3 = [100, 2]
    data_dict1 = {'v_d': 60, 't_d': 3}
    data_dict2 = {'v_d': 50, 't_d': 3}
    data_dict3 = {'v_d': 100, 't_d': 3}
    data_matrix = [data_list1, data_list2, data_list3]
    dicts_list = [data_dict1, data_dict2, data_dict3]

    if len(data_matrix) == len(dicts_list):
        for i in range(len(data_matrix)):
            print(f'{calculate_way(*data_matrix[i], **dicts_list[i])}\n')
