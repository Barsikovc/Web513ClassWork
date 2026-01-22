# my_string = "Hello World! Hello Python!"
# number_of_o_elements = my_string.count('o')
# print(number_of_o_elements)
#
# print(my_string[7:16])
# number_of_o_elements = my_string.count('o', 7, 16)
# print(number_of_o_elements)
#
# number_of_Hello_elements = my_string.count('Hello')
# print(number_of_Hello_elements)
#
# number_of_hello_elements = my_string.lower().count('hello')
# print(number_of_hello_elements)


# my_string = "Hello World! Hello Python!"
# element_idx = my_string.find('W')
# print(element_idx)
# element_idx = my_string.find('Python')
# print(element_idx)
# element_idx = my_string.find('Yello')
# print(element_idx)
# element_idx = my_string.find('Hello', 10, 20)
# print(element_idx)

# my_string = "Hello World! Hello Python! Hello Guido!"
# element_idx = my_string.rfind('e')
# print(element_idx)
# element_idx = my_string.rfind('Hello')
# print(element_idx)
# element_idx = my_string.rfind('Yello')
# print(element_idx)
# element_idx = my_string.rfind('Hello', 10, 20)
# print(element_idx)

my_string = "Hello World! Hello Python! Hello Guido!"
element_idx = my_string.index('W')
print(element_idx)
element_idx = my_string.index('Python')
print(element_idx)
# element_idx = my_string.index('Rython')
# print(element_idx)
element_idx = my_string.index('Hello', 10, 20)
print(element_idx)

my_string = "Hello World! Hello Python! Hello Guido!"
element_idx = my_string.rindex('e')
print(element_idx)
element_idx = my_string.rindex('Hello')
print(element_idx)
# element_idx = my_string.rindex('Rython')
# print(element_idx)
element_idx = my_string.rindex('Hello', 10, 20)
print(element_idx)


