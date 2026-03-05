import csv


def get_data_from_csv(file_path):
    csv_data = []
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            csv_data.append(row)

    return csv_data


def write_csv_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f'Запись прошла успешно!')


if __name__ == '__main__':
    my_data = get_data_from_csv(r'data_files\data.csv')
    print(my_data)
    for data_row in my_data:
        print(data_row)

    my_csv_data_visualize = [
        ['Name', 'Age', 'City'],
        ['Alice', '30', 'New York'],
        ['Bob', '25', 'Los Angeles'],
        ['Charlie', '35', 'Chicago']
    ]
    write_csv_file(r'data_files\csv_data_output.csv', my_csv_data_visualize)
