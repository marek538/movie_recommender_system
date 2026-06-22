import csv
import os
import random
import shutil

import CONSTANTS
from table_service import add_user
from table_service import update_ratings


genres = ['Drama', 'Crimi', 'Comedy', 'Mysterious', 'Thriller', 'Historical',
          'Action', 'Sci-Fi', 'Fantasy', 'Adventure', 'Horror', 'Western']

all_movies = []


def random_string():
    movie_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(10, 80)))
    return movie_name


def generate_random_movie_csv(filename, num_movies):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')

        writer.writerow(['Name'] + genres)

        for _ in range(num_movies):
            movie_name = random_string()
            all_movies.append(movie_name)
            movie_genres = [random.choice([0, 1]) for _ in genres]
            writer.writerow([movie_name] + movie_genres)


def generate_users(number):
    for i in range(number):
        username = random_string()
        add_user(username)
        for j in range(0, len(all_movies), 500):
            update_ratings(username, all_movies[j], random.randint(-1, 1))


# generate_random_movie_csv('resources/random_movies.csv', 500)
if os.path.exists(CONSTANTS.DIRECTORY_NAME):
    shutil.rmtree(CONSTANTS.DIRECTORY_NAME)
generate_users(1)

