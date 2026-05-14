class DBConnection:
    def __enter__(self):
        print(f'Открываем соединение с БД')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Закрываем соединение с БД')
        if exc_type:
            print(f'Произошла ошибка: {exc_val}')
        return True


class FileWriter:
    def __init__(self, filename):
        self.filename = filename
        self.mode = 'at'
        self.encoding = 'utf-8'
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            print(f'Ошибка в файле: {exc_val}')
        return True


if __name__ == '__main__':
    with DBConnection() as db, FileWriter(r'example_files\log.txt') as file:
        file.file.write("Запись в лог файл\n")
        print(f'Работаем с БД')
