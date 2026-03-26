"""
_ - защищенный
__ - приватный
"""


class Publication:

    def __init__(self, title, author, year):
        self._title = title
        self._author = author
        self._year = year

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    def display(self):
        print(f'Название: {self.title}')
        print(f'Автор: {self.author}')
        print(f'Год: {self.year}')


class Book(Publication):
    def __init__(self, title, author, year, code):
        super().__init__(title, author, year)
        self._code = code

    @property
    def code(self):
        return self._code

    def display(self):
        super().display()
        print(f'Код книги: {self.code}')


class Magazine(Publication):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self._issue_number = issue_number

    @property
    def issue_number(self):
        return self._issue_number

    def display(self):
        super().display()
        print(f'Номер выпуска: {self.issue_number}')


class Comix(Magazine):
    def __init__(self, title, author, year, issue_number, days=0):
        super().__init__(title, author, year, issue_number)
        self._days = days

    @property
    def days(self):
        return self._days

    @days.setter
    def days(self, days_num):
        if days_num.isdigit():
            self._days = int(days_num)
        else:
            print(f'Ошибка ввода допустимы только целые числа.')

    def display(self):
        super().display()
        if self.days == 0:
            print(f'Комикс находится в библиотеке')
        else:
            print(f'Комикс выдан на {self.days} дней')
