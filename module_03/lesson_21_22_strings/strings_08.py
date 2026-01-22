# string_alnum = '123abc'
# print(string_alnum.isalnum())
# string_alnum = '123abc*'
# print(string_alnum.isalnum())
#
# user_password = input('Введите желаемый пароль: ')
# if user_password.isalnum():
#     if 8 <= len(user_password) <= 12:
#         if user_password not in ['qwerty12345', '12345qwerty']:
#             print('Ваш пароль сохранен')
#         else:
#             print('Ваш пароль ненадежен')
#     else:
#         print('Длина пароля должна быть от 8 до 12 символов включительно')
# else:
#     print('Допустимы только буквы и цифры')


string_alpha = 'abcdfe'
print(string_alpha.isalpha())
string_alpha = 'abcdfe1234'
print(string_alpha.isalpha())
print()

string_digit = '1234567890'
print(string_digit.isdigit())

if string_digit.isdigit():
    print(int(string_digit))
print()

string_space = "  \n\t\r  "
print(string_space.isspace())
print()

string_lower = 'hello1234'
print(string_lower.islower())
string_lower = 'Hello1234'
print(string_lower.islower())
print()

string_upper = 'HELLO1234'
print(string_upper.isupper())
string_upper = 'Hello1234'
print(string_upper.isupper())
print()

string_title = "Hello World!"
print(string_title.istitle())
string_title = "hello World!"
print(string_title.istitle())
