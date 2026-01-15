start = 2
end = 11
step = 2
iteration = 1

for i in range(start, end, step):
    print(f'Значение i в итерации № {iteration} = {i}')
    iteration += 1
print()

start = 10
end = 0
step = -1
iteration = 1


for i in range(start, end, step):
    print(f'Значение i в итерации № {iteration} = {i}')
    iteration += 1
print()
