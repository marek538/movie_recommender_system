import time

from flask import Flask, render_template, request
import table_service
import user_data
from flask import Flask, jsonify, request, Blueprint
from global_state import PERSONAL_RECOMMENDATIONS

admin_page_blueprint = Blueprint('admin_page_blueprint', __name__)


@admin_page_blueprint.route('/admin', methods=['GET', 'POST'])
def admin_page():
    counting_idf_time = 0
    counting_recommendation_time = 0

    if request.method == 'POST':
        if 'count_idf' in request.form:
            print("Counting props")
            start_time = time.perf_counter()
            table_service.read_counted_norms()
            table_service.read_counted_idf()
            end_time = time.perf_counter()
            counting_idf_time = end_time - start_time
        elif 'count_recommendations' in request.form:
            print("Counting recommendations")
            all_users = table_service.read_user_table().columns[1:]

            start_time = time.perf_counter()
            for user in all_users:
                PERSONAL_RECOMMENDATIONS[user] = user_data.return_recommendations(user)

            end_time = time.perf_counter()
            counting_recommendation_time = end_time - start_time

    return render_template('admin_profile.html', counting_idf_time=counting_idf_time, counting_recommendation_time=counting_recommendation_time)
