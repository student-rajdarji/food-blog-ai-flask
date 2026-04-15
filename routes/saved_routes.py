from flask import Blueprint, render_template, redirect, flash, request
from flask_login import login_required, current_user
from db import db

saved_bp = Blueprint("saved", __name__)

# ----------------------------
# 📌 SHOW ALL SAVED RECIPES
# ----------------------------

@saved_bp.route("/saved-recipes")
@login_required
def saved_recipes():
    cursor = db.cursor(dictionary=True)

    # Relational join with blog table
    cursor.execute("""
        SELECT 
            saved_recipes.id AS saved_id,
            blog.id AS blog_id,
            blog.title,
            blog.slug,
            blog.image_url
        FROM saved_recipes
        JOIN blog ON saved_recipes.blog_id = blog.id
        WHERE saved_recipes.user_id = %s
        ORDER BY saved_recipes.id DESC
    """, (current_user.id,))

    blog_recipes = cursor.fetchall()

    # AI recipes
    cursor.execute("""
        SELECT id, title FROM saved_ai_recipes
        WHERE user_id=%s
        ORDER BY id DESC
    """, (current_user.id,))
    ai_recipes = cursor.fetchall()

    return render_template(
        "saved_recipes.html",
        blog_recipes=blog_recipes,
        ai_recipes=ai_recipes
    )
# ----------------------------
# 🤖 VIEW FULL AI RECIPE
# ----------------------------
@saved_bp.route("/view-ai-recipe/<int:id>")
@login_required
def view_ai_recipe(id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT title, recipe FROM saved_ai_recipes
        WHERE id=%s AND user_id=%s
    """, (id, current_user.id))
    recipe = cursor.fetchone()

    if not recipe:
        flash("AI Recipe not found", "danger")
        return redirect("/saved-recipes")

    return render_template("view_ai_recipe.html", recipe=recipe)

@saved_bp.route("/remove-saved/<int:id>", methods=["POST"])
@login_required
def remove_saved(id):
    cursor = db.cursor()
    cursor.execute("""
        DELETE FROM saved_recipes
        WHERE id = %s AND user_id = %s
    """, (id, current_user.id))

    db.commit()
    flash("Recipe removed ❤️", "success")
    return redirect("/saved-recipes")   # <-- SAFE REDIRECT

@saved_bp.route("/view-saved-recipe/<int:id>")
@login_required
def view_saved_recipe(id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT title, content
        FROM saved_recipes
        WHERE id=%s AND user_id=%s
    """, (id, current_user.id))
    recipe = cursor.fetchone()

    if not recipe:
        flash("Recipe not found", "danger")
        return redirect("/saved-recipes")

    return render_template("view_saved_recipe.html", recipe=recipe)