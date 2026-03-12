class Book:
    def __init__(self, title, author, year=None):
        self.title = title
        self.author = author
        if not year:
            self.year = 'Не указано'
        else:
            self.year = year


if __name__ == '__main__':
    book = Book('Дубровский', 'Пушкин А.С.')
    print(book.title)
    print(book.author)
    print(book.year)
    print()

    book.title = "Странный Человек"
    book.author = "Лермонтов М.В."
    print(book.title)
    print(book.author)
