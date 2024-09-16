from flask import render_template
from plantspire import app, db
from plantspire.models import Recipes, Categories


@app.route("/")
def home():
    return render_template("base.html")