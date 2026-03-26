from Classes.ClassesPublications import Publication, Book, Magazine, Comix

if __name__ == '__main__':
    publication = Publication('Все о слонах', 'Научная библиотека', "2005")
    publication.display()
    print()

    book = Book("Дубровский", 'Пушкин А.С.', "1998", '9885')
    book.display()
    print()

    magazine = Magazine('Вокруг Света', 'Коллектив Авторов', '2005', '11-2005')
    magazine.display()
    print()

    comix = Comix('Человек Паук', 'Стэн Ли', '1995', '95-01')
    comix.display()
    comix.days = "10"
    comix.display()
    print()
