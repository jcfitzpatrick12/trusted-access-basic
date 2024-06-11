from flask import render_template

from app import create_app
from app.users.views import users_blueprint
from app.manage.views import manage_blueprint

flask_app = create_app()
flask_app.register_blueprint(users_blueprint)
flask_app.register_blueprint(manage_blueprint)


@flask_app.route('/')
def index():  # put application's code here
    return render_template('main/index.html')

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=5000, debug=True)