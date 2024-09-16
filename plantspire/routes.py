from flask import render_template
from plantspire import app, db
from plantspire.models import Recipes, Categories


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/")
def get_recipes():
    return render_template("recipes.html")


@app.route("/")
def add_recipes():
    return render_template("add-recipes.html")


@app.route("/")
def get_categories():
    return render_template("categories.html")


@app.route("/")
def add_category ():
    return render_template("add-category.html")


@app.route("/")
def profile ():
    return render_template("profile.html")


@app.route("/")
def login ():
    return render_template("login.html")


@app.route("/")
def logout ():
    return render_template("logout.html")


@app.route("/")
def register ():
    return render_template("register.html")




