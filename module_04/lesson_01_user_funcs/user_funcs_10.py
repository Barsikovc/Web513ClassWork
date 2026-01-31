import random


def get_random_genre(genre, genres_data):
    if genre == '1':
        return f'Мы смотрим фильм в жанре: {random.choice(genres_data[0])}'
    elif genre == '2':
        return f'Мы читаем книгу в жанре: {random.choice(genres_data[1])}'
    elif genre == '3':
        return f'Мы играем в игру в жанре: {random.choice(genres_data[2])}'
    else:
        return f'Неизвестный жанр'


if __name__ == '__main__':
    cinema_genres = ["Драма", "Комедия", "Фэнтези", "Ужасы"]
    book_genres = ["Поэма", "Водевиль", "Роман", "Проза"]
    game_genres = ["Симулятор", "Аркада", "RPG", "Инди"]
    my_genres_data = [cinema_genres, book_genres, game_genres]

    while True:
        user_genre = input('Что будем делать: 1 - кино; 2 - книги; 3 - игры; 0 - выход: ')
        if user_genre == '0':
            print('Программа завершила свою работу.')
            break
        print(get_random_genre(user_genre, my_genres_data))
