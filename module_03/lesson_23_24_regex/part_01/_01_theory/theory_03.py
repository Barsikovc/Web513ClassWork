import re

# print('Введите номер телефона в формате:\n+***(**)******* для РБ\n+*(***)******* для РФ')
phone_number = "Мой номер телефона +375(29)1234567 или +7(922)1234567"

pattern = re.compile(r'\+\d{1,3}\(\d{2,3}\)\d{7}')
print(re.findall(pattern, phone_number))
user_phone = input('Введите номер телефона в формате:\n+***(**)******* для РБ\n+*(***)******* для РФ:\n')
print(bool(re.match(pattern, user_phone)))
