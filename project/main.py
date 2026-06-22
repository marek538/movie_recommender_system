import os

from flask import Flask, render_template, request, Blueprint

import CONSTANTS
import table_service
import user_data

from user_profile import user_page_blueprint
from admin_profile import admin_page_blueprint
from add_user import add_user_blueprint
from user_rating_page import rating_blueprint
from global_state import PERSONAL_RECOMMENDATIONS

app = Flask(__name__)


app.register_blueprint(user_page_blueprint)
app.register_blueprint(add_user_blueprint)
app.register_blueprint(rating_blueprint)
app.register_blueprint(admin_page_blueprint)


@app.route('/')
def home():

    users = table_service.read_user_table()
    user_names = users.columns[1:].tolist()
    #for user in user_names:
    #    PERSONAL_RECOMMENDATIONS[user] = []

    return render_template('main_menu.html', user_names=user_names)


if __name__ == '__main__':
    if not os.path.exists(CONSTANTS.DIRECTORY_NAME):
        os.makedirs(CONSTANTS.DIRECTORY_NAME)

    table_service.count_idf()
    app.run(debug=True)
