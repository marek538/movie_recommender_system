from flask import Flask, render_template, request
import table_service
import user_data
from flask import Flask, jsonify, request, Blueprint
from global_state import PERSONAL_RECOMMENDATIONS

user_page_blueprint = Blueprint('first_blueprint', __name__)

@user_page_blueprint.route('/<username>')
def user_page(username):
    if username not in PERSONAL_RECOMMENDATIONS:
        top_movies = {}
    else:
        top_movies = PERSONAL_RECOMMENDATIONS[username]

    return render_template('user_profile.html', top_movies=top_movies, username=username)

