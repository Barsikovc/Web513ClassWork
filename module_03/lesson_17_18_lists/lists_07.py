# # замена значений
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Action"]
# cinema_genres[1] = "Scy-Fy"
# print(cinema_genres)
#
# # slices/срезы
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Action", "Scy-Fy", "Horror"]
# cinema_genres_slice = cinema_genres[2:4]
# print(cinema_genres_slice)
#
# cinema_genres_slice_from_beginning = cinema_genres[:4]
# print(cinema_genres_slice_from_beginning)
# cinema_genres_slice_till_end = cinema_genres[2:]
# print(cinema_genres_slice_till_end)
# # print(cinema_genres)
# cinema_genres_slice_step = cinema_genres[::2]
# print(cinema_genres_slice_step)
# cinema_genres_slice_all = cinema_genres[:]
# print(cinema_genres_slice_all)


# оператор принадлежности in
cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
print('Comedy' in cinema_genres)
print('Detective' in cinema_genres)
print()

# del
cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
del cinema_genres[2]
print(cinema_genres)