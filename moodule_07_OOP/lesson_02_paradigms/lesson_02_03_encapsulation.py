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

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def set_year(self, new_year):
        if isinstance(new_year, str) and new_year.isdigit():
            self.__year = new_year
            print(f'Год успешно изменен')
        else:
            raise ValueError('Год может быть только целым числом.')


if __name__ == '__main__':
    book = Book('Дубровский', 'Пушкин А.С.')
    print(book.get_title())
    print(book.get_author())
    print(book.get_year())
    print()

    book.set_year('1995')
    print(book.get_year())
    book.set_year('abcd')