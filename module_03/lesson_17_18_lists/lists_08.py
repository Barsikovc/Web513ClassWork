# cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
# new_cinema_genres = cinema_genres
#
# new_cinema_genres.append('Scy-Fy')
# print(new_cinema_genres)
# print(cinema_genres)
#
# print(cinema_genres == new_cinema_genres)
# print(cinema_genres is new_cinema_genres)
# print()

cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
new_cinema_genres = cinema_genres[:]
print(cinema_genres == new_cinema_genres)
print(cinema_genres is new_cinema_genres)
new_cinema_genres.append('Scy-Fy')
print(new_cinema_genres)
print(cinema_genres)
print()

cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
new_cinema_genres = list(cinema_genres)
print(cinema_genres == new_cinema_genres)
print(cinema_genres is new_cinema_genres)
print()

cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
for genre in cinema_genres[:]:
    if genre == 'Fantasy':
        cinema_genres.remove('Fantasy')
print(cinema_genres)

cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
new_cinema_genres = cinema_genres.copy()
print(cinema_genres == new_cinema_genres)
print(cinema_genres is new_cinema_genres)
print()


