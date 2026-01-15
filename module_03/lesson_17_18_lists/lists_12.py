import random

cinema_genres = ["Drama", "Comedy", "Fantasy", "Horror", "Romance"]

index = random.randint(0, len(cinema_genres) - 1)
genre = cinema_genres[index]
print(f'Ваш случайный жанр: {genre}.\n')

random.shuffle(cinema_genres)
genre = cinema_genres[0]
print(f'Ваш случайный жанр: {genre}.\n')

genre = random.sample(cinema_genres, 1)
print(f'Ваш случайный жанр: {genre[0]}.\n')

genre = random.choice(cinema_genres)
print(f'Ваш случайный жанр: {genre}.\n')
