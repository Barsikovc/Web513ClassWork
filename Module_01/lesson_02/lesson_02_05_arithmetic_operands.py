print(3 + 5)
print(5 - 3)
print(3 * 5)
print(3 ** 3)
print(6 / 3)
print()

print(11 // 3)
print(11 % 3)

num_4_digits = 1234
digit1 = 1234 // 1000
digit2 = 1234 % 1000 // 100
digit3 = 1234 % 1000 % 100 // 10
digit4 = 1234 % 1000 % 100 % 10
print(digit1, digit2, digit3, digit4, sep=', ')
print(digit1 + digit2 + digit3 + digit4)
print()


num_1 = 10
if num_1 % 2 == 0:
    print('even')
else:
    print('odd')
