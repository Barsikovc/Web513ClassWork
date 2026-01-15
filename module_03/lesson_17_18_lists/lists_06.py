# cinema_genres = ["Drama", "Comedy", "Fantasy", "Action"]
# book_genres = ["Detective", "Poem", "Scy-Fy", "Fantasy"]
#
# # работа с циклами
# for genre in cinema_genres:
#     print(genre)
# print()
#
# if len(cinema_genres) == len(book_genres):
#     for idx in range(len(cinema_genres)):
#         print(f'{idx}: {cinema_genres[idx]}')
#         print(f'{idx}: {book_genres[idx]}')
# else:
#     print(f'Списки разной длины при итерации возможны ошибки')
# print()
#
# for idx, item in enumerate(cinema_genres):
#     print(idx, item)
# print()
#

# # метод .append()
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Action"]
# book_genres = ["Detective", "Poem", "Scy-Fy", "Fantasy"]
# cinema_genres.append('Historic')
# book_genres.append('Novel')
# print(cinema_genres, book_genres)

# # метод .extend()
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Action"]
# genres_to_add = ['Historic', 'Scy-Fy']
# cinema_genres.extend(genres_to_add)
# print(cinema_genres)

# # метод .insert()
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Action"]
# cinema_genres.insert(2, 'Scy-Fy')
# print(cinema_genres)

# # метод .remove()
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Action", "Fantasy"]
# for genre in cinema_genres[:]:
#     if genre == 'Fantasy':
#         cinema_genres.remove('Fantasy')
# print(cinema_genres)


# # метод .pop()
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Action"]
# popped_item = cinema_genres.pop()
# print(popped_item)
# print(cinema_genres)
#
# popped_item_idx = cinema_genres.pop(1)
# print(popped_item_idx)
# print(cinema_genres)

# # метод .clear()
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Comedy", "Action", "Comedy"]
# cinema_genres.clear()
# print(cinema_genres)


# # метод .index()
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Comedy", "Action", "Comedy"]
# print(cinema_genres.index('Comedy'))
#
# item_idx = 0
# for genre in cinema_genres:
#     if genre == 'Comedy':
#         print(item_idx)
#     item_idx += 1
#
#
# for idx, genre in enumerate(cinema_genres):
#     if genre == 'Comedy':
#         print(idx)
#
# item1, item2 = ["Drama", "Comedy"]
# print(item1)
# print(item2)

# # метод .count()
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Comedy", "Action", "Comedy"]
# print(cinema_genres.count('Comedy'))

cinema_genres = ["Drama", "Comedy", "Fantasy", "Comedy", "Action"]
cinema_genres.sort()
print(cinema_genres)
cinema_genres.sort(reverse=True)
print(cinema_genres)

cinema_genres = ["Drama", "Comedy", "Fantasy", "Comedy", "Action"]
cinema_genres.reverse()
print(cinema_genres)
