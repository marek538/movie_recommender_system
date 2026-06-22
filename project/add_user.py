from flask import Flask, render_template, request
import table_service
import user_data
from flask import Flask, jsonify, request, Blueprint

add_user_blueprint = Blueprint('add_user_blueprint', __name__)


@add_user_blueprint.route('/add_user', methods=['POST'])
def add_user():
    user_name = request.form['user_name']
    if table_service.add_user(user_name):
        return render_template('add_user.html', to_print='User added')
    else:
        return render_template('add_user.html', to_print='User already exists')
