"""
_ - защищенный
__ - приватный
"""


class Book:
    def __init__(self, title, author, year=None):
        self.__title = title
        self.__author = author
        if not year:
            self.__year = 'Не указано'
        else:
            self.__year = year

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        if isinstance(new_year, str) and new_year.isdigit():
            self.__year = new_year
            print(f'Год успешно изменен')
        else:
            raise ValueError('Год может быть только целым числом.')


if __name__ == '__main__':
    book = Book('Дубровский', 'Пушкин А.С.')
    print(book.title)
    print(book.author)
    print(book.year)
    print()

    book.year = '1995'
    print(book.year)
    # book.year('abcd')