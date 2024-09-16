from plantspire import db

class Recipes(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.Text)
    ingredients = db.Column("ingredients", db.Text)
    directions = db.Column("directions", db.Text)
    categories = db.Column("categories", db.Text)
    desc = db.Column("desc", db.Text)
    rating = db.Column("rating", db.Integer)
    image = db.Column("image", db.Text)

    def __init__(
        self,
        title,
        ingredients,
        directions,
        categories,
        desc,
        rating,
    ):
        self.title = title
        self.ingredients = ingredients
        self.directions = directions
        self.categories = categories
        self.desc = desc
        self.rating = rating


class Categories(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    categories = db.Column("categories", db.Text)

    def __init__(self, categories):
        self.categories = categories