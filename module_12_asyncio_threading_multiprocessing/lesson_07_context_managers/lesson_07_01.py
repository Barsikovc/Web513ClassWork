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
        data = self.file.read()
        return data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Если возвращаем True, исключение не будет поднято
        return True


if __name__ == '__main__':
    with FileWorker(r'example_files\example01.txt', mode='w', encoding='utf-8') as writer:
        writer.write('Hello World!\n')
        writer.write('Привет мир\n')

    with FileWorker(r'example_files\example01.txt', mode='r', encoding='utf-8') as reader:
        data = reader.read()
    print(data)
