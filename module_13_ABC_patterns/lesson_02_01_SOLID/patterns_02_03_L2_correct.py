"""
L - Liskov Substitution Principle
Принцип подстановки Лисков
"""


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


class WritableDocument(Document):
    def save_document(self, new_data, method):
        if method == 'rewrite':
            mode = 'w'
        else:
            mode = 'a'
        with open(self.filename, mode, encoding='utf-8') as file:
            file.write(new_data)


if __name__ == '__main__':
    document = Document(r'documents\SOLID.txt')
    print(document.open_document())
    print()

    wr_document = WritableDocument(r'documents\SOLID.txt')
    print(wr_document.open_document())
    print()

    wr_document.save_document('new_data', 'rewrite')
    print(wr_document.open_document())
    print()

    wr_document.save_document('\nadded_data', 'append')
    print(wr_document.open_document())
