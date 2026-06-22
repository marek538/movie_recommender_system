from flask import Flask, render_template, request
import table_service
import user_data
from flask import Flask, jsonify, request, Blueprint
import pandas as pd
import numpy as np
import CONSTANTS
from flask import request, redirect, url_for

rating_blueprint = Blueprint('rating_blueprint', __name__)

@rating_blueprint.route('/<username>/rating', methods=['GET', 'POST'])
def user_page(username):
    all_movies = table_service.read_movies_table()[table_service.CONSTANTS.FILM_COLUMN_NAME]
    user_ratings = table_service.read_user_table()[username]

    searchSpec = request.args.get("searchSpec", "").strip()

    if request.method == 'POST':
        for movie in all_movies:
            new_rating = request.form.get(movie)
            if new_rating:
                table_service.update_ratings(username, movie, int(new_rating))
        return redirect(url_for('rating_blueprint.user_page', username=username))

    movie_ratings = list(zip(all_movies, user_ratings))

    if searchSpec:
        movie_ratings = [(movie, rating) for movie, rating in movie_ratings if searchSpec.lower() in movie.lower()]

    return render_template('user_ratings.html', movie_ratings=movie_ratings, username=username, searchSpec=searchSpec)

