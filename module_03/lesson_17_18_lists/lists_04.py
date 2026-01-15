even_square_list = [i * i for i in range(1, 11) if i % 2 == 0]
print(even_square_list)

even_square_list_simple = []
for i in range(1, 11):
    if i % 2 == 0:
        even_square_list_simple.append(i * i)
print(even_square_list_simple)
print()

customers = ["Bob", "Joe", "Anna", "Bob", "Nick"]
customers_filtered = [customer for customer in customers if customer != 'Bob' and customer != 'Joe']
print(customers_filtered)

customers_filtered_simple = []
for customer in customers:
    if customer != 'Bob' and customer != 'Joe':
        customers_filtered_simple.append(customer)
print(customers_filtered_simple)
print()

product_list = [i * j for i in range(1, 4) for j in range(1, 5)]
print(product_list)

product_list_simple = []
for i in range(1, 4):
    for j in range(1, 5):
        product_list_simple.append(i * j)
print(product_list_simple)
print()

my_data = [[i * j for i in range(1, 4)] for j in range(1, 5)]
print(my_data)

# [
# [1, 2, 3],
# [2, 4, 6],
# [3, 6, 9],
# [4, 8, 12]
# ]

my_matrix_simple = []
for j in range(1, 5):
    row = []
    for i in range(1, 4):
        row.append(i * j)
    my_matrix_simple.append(row)
print(my_matrix_simple)