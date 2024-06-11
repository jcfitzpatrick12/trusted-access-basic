from flask import Blueprint, render_template


manage_blueprint = Blueprint('manage', __name__, template_folder='templates')


@manage_blueprint.route('/manage_access')
def manage_access():
    return render_template('manage/manage_access.html')

@manage_blueprint.route('/give_access')
def give_access():
    return render_template('manage/give_access.html')