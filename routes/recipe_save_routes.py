from flask import Blueprint, request, redirect, flash, render_template
from flask_login import login_required, current_user
import mysql.connector

recipe_save_bp = Blueprint("recipe_save", __name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rajdarji@3456",
    database="food_blog_ai"
)

cursor = db.cursor(dictionary=True)

# ✅ SAVE RECIPE
@recipe_save_bp.route("/save-recipe", methods=["POST"])
@login_required
def save_recipe():
    recipe = request.form.get("recipe")

    cursor.execute(
        "INSERT INTO ai_saved_recipes (user_id, recipe) VALUES (%s, %s)",
        (current_user.id, recipe)
    )
    db.commit()

    flash("Recipe saved successfully ❤️", "success")
    return redirect("/ai-generator")

# ✅ SHOW SAVED RECIPES
@recipe_save_bp.route("/my-ai-recipes")
@login_required
def my_ai_recipes():
    cursor.execute(
        "SELECT * FROM ai_saved_recipes WHERE user_id = %s ORDER BY created_at DESC",
        (current_user.id,)
    )
    recipes = cursor.fetchall()
    return render_template("my_saved_ai_recipes.html", recipes=recipes)