import pandas as pd
import numpy as np
import table_service

import CONSTANTS


# used in return_recommendations
def count_profile(name):
    normalized_df = table_service.read_counted_norms()
    user_df = table_service.read_user_table()

    rating_vector = user_df[name].values
    profile = normalized_df.iloc[:, 1:].multiply(rating_vector, axis=0).sum()
    # print("Profile:", profile)
    return profile


# used in return_recommendations
def count_score(profile):
    object_weights = table_service.read_counted_norms()

    idf = table_service.read_counted_idf()

    idf_values = idf.values.flatten()

    object_weights.set_index(CONSTANTS.FILM_COLUMN_NAME, inplace=True)
    weighted_objects = object_weights * idf_values
    print(weighted_objects)
    score = weighted_objects.dot(profile)
    score = pd.Series(score, index=object_weights.index)
    print("Score:", score)
    return score

def return_recommendations(name):
    profile = count_profile(name)
    score = count_score(profile)

    tmp = table_service.read_user_table()

    filtered_names = tmp[tmp[name] == 0][CONSTANTS.FILM_COLUMN_NAME]

    filtered_scores = score.loc[filtered_names]

    sorted_filtered = filtered_scores.sort_values(ascending=False)

    return dict(sorted_filtered[:10])
