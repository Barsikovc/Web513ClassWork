"""
L - Liskov Substitution Principle
Принцип подстановки Лисков
"""


class ReadOnlyError(Exception):
    pass


class Document:
    def __init__(self, filename, data=None):
        self.filename = filename
        self.data = data

    def open_document(self):
        try:
            with open(self.filename, encoding='utf-8') as file:
                self.data = file.read()
                return self.data
        except FileNotFoundError:
            print(f'Файл не найден')
            return None

    def save_document(self, new_data, method):
        if method == 'rewrite':
            mode = 'w'
        else:
            mode = 'a'
        with open(self.filename, mode, encoding='utf-8') as file:
            file.write(new_data)


class ReadOnlyDocument(Document):
    def save_document(self, new_data, method):
        try:
            raise ReadOnlyError
        except ReadOnlyError:
            print(f'Только для чтения')


if __name__ == '__main__':
    document = Document(r'documents\NO_SOLID.txt')
    print(document.open_document())
    print()
    document.save_document('new_data', 'rewrite')
    print(document.open_document())
    print()
    document.save_document('\nadded_data', 'append')
    print(document.open_document())
    print()
