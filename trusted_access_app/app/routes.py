from flask import current_app as app

@app.route('/index.html')
def index():
    return "Hello Reboot2024!"

