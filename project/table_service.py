import pandas as pd
from pathlib import Path
import numpy as np
import os

import CONSTANTS


def read_movies_table():
    if not os.path.exists(CONSTANTS.MOVIES_PATH):
        raise FileNotFoundError(f"File not found: {CONSTANTS.MOVIES_PATH}")

    df = pd.read_csv(CONSTANTS.MOVIES_PATH, delimiter=';')
    return df


def read_user_table():
    if not os.path.exists(CONSTANTS.DIRECTORY_NAME):
        os.makedirs(CONSTANTS.DIRECTORY_NAME)

    if not os.path.exists(CONSTANTS.USER_PATH):
        create_user_table()

    df = pd.read_csv(CONSTANTS.USER_PATH, delimiter=';')
    return df


def read_counted_norms():
    if not os.path.exists(CONSTANTS.DIRECTORY_NAME):
        os.makedirs(CONSTANTS.DIRECTORY_NAME)

    if not os.path.exists(CONSTANTS.COUNTED_NORMS_PATH):
        normalize_movies_table()

    df = pd.read_csv(CONSTANTS.COUNTED_NORMS_PATH, delimiter=';')
    return df


def read_counted_idf():
    if not os.path.exists(CONSTANTS.DIRECTORY_NAME):
        os.makedirs(CONSTANTS.DIRECTORY_NAME)

    if not os.path.exists(CONSTANTS.COUNTED_IDF_PATH):
        count_idf()

    df = pd.read_csv(CONSTANTS.COUNTED_IDF_PATH, delimiter=';')
    return df


def normalize_movies_table():
    print("Normalizing table")

    df = read_movies_table()

    norms = np.linalg.norm(df.iloc[:, 1:], axis=1)

    normalized_df = df.copy()
    normalized_df.iloc[:, 1:] = df.iloc[:, 1:].div(norms, axis=0)

    normalized_df.to_csv(CONSTANTS.COUNTED_NORMS_PATH, index=False, sep=';')


def count_idf():
    if not os.path.exists(CONSTANTS.DIRECTORY_NAME):
        os.makedirs(CONSTANTS.DIRECTORY_NAME, exist_ok=True)

    print("Counting idf")

    df = read_movies_table()
    sums = df.iloc[:, 1:].sum().to_frame().T

    # divide by 0
    idf = np.where(sums == 0, 0, np.log10(df.shape[0] / sums))

    idf_df = pd.DataFrame(idf, columns=sums.columns)
    idf_df.to_csv(CONSTANTS.COUNTED_IDF_PATH, sep=";", index=False)


def create_user_table():
    df = read_movies_table()

    user_df = pd.DataFrame({CONSTANTS.FILM_COLUMN_NAME: df[CONSTANTS.FILM_COLUMN_NAME]})

    user_df.to_csv(CONSTANTS.USER_PATH, sep=';', index=False)


def add_user(user_name):
    # print("Adding user", user_name)
    if not Path(CONSTANTS.USER_PATH).exists:
        create_user_table()

    if user_name in read_user_table().columns:
        return False
    df = read_user_table()
    df[user_name] = [0] * df.shape[0]
    df.to_csv(CONSTANTS.USER_PATH, index=False, sep=';')
    return True


def update_ratings(user_name, movie_name, rating):

    if not Path(CONSTANTS.USER_PATH).exists or Path(CONSTANTS.USER_PATH).stat().st_size == 0:
        create_user_table()
        add_user(user_name)
    df = read_user_table()
    df.loc[df[CONSTANTS.FILM_COLUMN_NAME] == movie_name, user_name] = rating
    df.to_csv(CONSTANTS.USER_PATH, index=False, sep=';')
