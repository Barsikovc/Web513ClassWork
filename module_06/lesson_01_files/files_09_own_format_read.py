def get_data_dict_from(filename, divider):
    managers_dict = {}
    with open(filename, encoding='utf-8') as managers_data:
        for manager_data in managers_data:
            clean_data = manager_data.strip().split(divider)
            # manager = clean_data[0]
            # company = clean_data[1]
            # head_company = clean_data[2]
            manager, company, head_company = clean_data
            managers_dict[(company, head_company)] = manager
    return managers_dict


if __name__ == '__main__':
    managers_filename = r'data_files\managers_data_own_format.txt'
    managers_data_dict = get_data_dict_from(managers_filename, ':')
    for (company, head_company), manager in managers_data_dict.items():
        print(f'{manager} работает в компании {company} которая принадлежит {head_company}')
