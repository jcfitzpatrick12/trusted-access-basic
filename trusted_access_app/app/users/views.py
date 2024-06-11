from flask import Blueprint, render_template


users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/profile')
def profile():
    return render_template('users/profile.html')
