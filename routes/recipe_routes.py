from flask import Blueprint, render_template
from models.blog import Blog

recipe_bp = Blueprint("recipe", __name__)

@recipe_bp.route("/recipes")
def recipes():
    recipes = Blog.query.order_by(Blog.id.desc()).all()
    return render_template("recipes/recipes.html", recipes=recipes)