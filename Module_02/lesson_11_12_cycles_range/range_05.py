for i in range(5):
    if i == 3:
        break
    print(f'i = {i}')
print()


for i in range(10):
    if i == 3 or i == 7:
        continue
    print(f'i = {i}')
print()

for i in range(10):
    if i == 3 or i == 7:
        pass
    print(f'i = {i}')
print()

for i in range(10):
    if i == 12:
        break
    print(f'i == {i}')
else:
    print('Цикл завершен без прерываний.')
print()

for i in range(10):
    if i == 5:
        break
    print(f'i == {i}')
else:
    print('Цикл завершен без прерываний.')
print()

