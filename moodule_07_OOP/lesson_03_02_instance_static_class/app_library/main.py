from classes.ClassBook import LibraryBook

if __name__ == '__main__':
    LibraryBook.display_all_books()
    book1 = LibraryBook('Мастер и Маргарита')
    book2 = LibraryBook("1984")
    print(book1)
    print(book2)
    book1.change_status('выдана')
    print(book1)
    print()
    LibraryBook.display_all_books()
    print(LibraryBook.is_available(book1))
    print(LibraryBook.is_available(book2))
