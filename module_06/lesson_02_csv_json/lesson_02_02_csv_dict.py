import csv


def get_data_from_csv_dict(file_path):
    csv_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_data.append(row)
    return csv_data


def analyse_sales(data_list: list[dict[str, str]]):
    total_revenue = 0
    data_analyses = []
    for data in data_list:
        product = data['product']
        product_revenue = int(data['quantity']) * float(data['price'])
        total_revenue += product_revenue
        product_data = [product, product_revenue]
        data_analyses.append(product_data)

    return data_analyses, total_revenue


if __name__ == '__main__':
    my_csv_data = get_data_from_csv_dict(r'data_files\sales_data.csv')
    print(my_csv_data)

    my_data, my_revenue = analyse_sales(my_csv_data)
    for row_data in my_data:
        print(row_data)
    print(my_revenue)
