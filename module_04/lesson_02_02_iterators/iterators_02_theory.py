numbers = [1, 2, 3]  # Итерируемый объект
iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
        input('Нажмите ввод для получения следующего элемента')
    except StopIteration:
        break
