mutable_tuple = ([1, 2, 3], [4, 5, 6])
print(f"Исходный кортеж: {mutable_tuple}")

mutable_tuple[0][1] = 10
mutable_tuple[1].append(7)

print(f"Измененный кортеж: {mutable_tuple}")

