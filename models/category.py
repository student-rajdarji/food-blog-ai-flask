from extensions import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # relationship to connect recipes
    recipes = db.relationship("Recipe", backref="category", lazy=True)
