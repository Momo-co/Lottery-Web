from application import app, db
from flask import redirect, request, render_template, url_for
from application.models import Record

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')