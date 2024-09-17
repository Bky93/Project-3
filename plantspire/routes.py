from flask import Flask, render_template
from plantspire import app, db
from plantspire.models import Recipes, Categories


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/get_recipes")
def get_recipes():
    return render_template("recipes.html")


@app.route("/add_recipes")
def add_recipes():
    return render_template("add-recipes.html")


@app.route("/get_categories")
def get_categories():
    return render_template("categories.html")


@app.route("/add_category")
def add_category ():
    return render_template("add-category.html")


@app.route("/profile")
def profile ():
    return render_template("profile.html")


@app.route("/login")
def login ():
    return render_template("login.html")


@app.route("/logout")
def logout ():
    return render_template("logout.html")


@app.route("/register")
def register ():
    return render_template("register.html")




