with open(r'files\students.txt', 'rt', encoding='utf-8') as file:
    data = file.readlines()

# print(data)
print('Первые 10 строк')
print(''.join(data[:10]))
print()

# Используем итератор для чтения файла построчно
with open(r'files\students.txt', 'rt', encoding='utf-8') as file:
    iterator = iter(file)
    for _ in range(10):
        print(next(iterator).rstrip())
        input('Нажмите ввод для получения следующей строки')
print()

# Используем итератор для чтения файла построчно
with open(r'files\students.txt', 'rt', encoding='utf-8') as file:
    counter = 0
    for line in file:
        if counter == 10:
            break
        counter += 1
        print(line.rstrip())
print()
