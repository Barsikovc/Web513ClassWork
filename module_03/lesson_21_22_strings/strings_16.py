import random
import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.octdigits)
# print(string.hexdigits)
# print(string.punctuation)
# print(string.printable)


user_login1 = ''.join(random.choices(string.ascii_lowercase, k=8))
user_login2 = ''.join(random.sample(string.ascii_lowercase, k=8))

user_password1 = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
user_password2 = ''.join(random.sample(string.ascii_letters + string.digits, k=12))

print(f"Login1: {user_login1}")
print(f'Password1: {user_password1}')
print()
print(f"Login2: {user_login2}")
print(f'Password2: {user_password2}')
