"""
Задание 1. Работа с файлами

Ситуация: мы работаем с текстовыми файлами и часто открываем и закрываем их.
Чтобы избежать ошибок, связанных с забытым закрытием файла, используем менеджеры контекста.

Задача — написать код, который создаёт файл, записывает в него строку,
а затем считывает содержимое и выводит на экран. Использовать конструкцию with для работы с файлом.

Шаги реализации:

1) Создадим файл с использованием менеджера контекста.
2) Запишем текст в файл.
3) Считаем текст из файла и выведем его.
"""


class FileWorker:
    def __init__(self, filename, mode='rt', encoding=None):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self

    def write(self, data):
        self.file.write(data)

    def read(self):
        return self.file.read()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f'Ошибка: {exc_type.__name__}: {exc_val}')
            return False
        self.file.close()
        return True


if __name__ == '__main__':
    with FileWorker(r'example_files\example.txt', mode='a', encoding='utf-8') as writer:
        writer.write('Hello World!\n')
        writer.write('Привет мир\n')

    with FileWorker(r'example_files\example.txt', encoding='utf-8') as reader:
        data = reader.read()
        # raise Exception('Произошла ошибка при чтении файла')
    print(data)

