import random

cinema_genres = ["Drama", "Comedy", "Fantasy", "Horror", "Romance"]
print(cinema_genres)
random.shuffle(cinema_genres)
print(cinema_genres)

cinema_genres = ["Drama", "Comedy", "Fantasy", "Horror", "Romance"]
genres_sample = random.sample(cinema_genres, 3)
print(genres_sample)

# some_str = 'Привет я строка!'
# sample_str = random.sample(some_str, len(some_str))
# print(sample_str)
# result = ''.join(sample_str)
# print(result)

cinema_genres = ["Drama", "Comedy", "Fantasy", "Horror", "Romance"]
random_genre = random.choice(cinema_genres)
print(random_genre)

cinema_genres = ["Drama", "Comedy", "Fantasy", "Horror", "Romance"]
random_genre = random.choices(cinema_genres, k=10)
print(random_genre)
