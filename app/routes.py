from app import app
from flask import redirect, render_template, url_for

@app.route("/index")
def index():
    return redirect(url_for('root'))

@app.route("/")
def root():
    return render_template("root.html")