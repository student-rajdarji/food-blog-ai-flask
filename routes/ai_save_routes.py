from flask import Blueprint, request, redirect, flash, url_for
from flask_login import login_required, current_user
from db import db

ai_save_bp = Blueprint("ai_save", __name__)

@ai_save_bp.route("/save-ai-recipe", methods=["POST"])
@login_required
def save_ai_recipe():
    print("FORM DATA:", request.form)

    title = request.form.get("title")
    recipe = request.form.get("recipe")

    if not title or not recipe:
        flash("Invalid AI recipe", "danger")
        return redirect(url_for("ai.ai_generator"))

    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO saved_ai_recipes (user_id, title, recipe)
        VALUES (%s, %s, %s)
    """, (current_user.id, title, recipe))

    db.commit()

    flash("AI Recipe saved ❤️", "success")
    return redirect(url_for("saved.saved_recipes"))


@ai_save_bp.route("/delete-ai-recipe/<int:id>", methods=["POST"])
@login_required
def delete_ai_recipe(id):
    cursor = db.cursor()   # ✅ FIX 1: create cursor

    cursor.execute(
        """
        DELETE FROM saved_ai_recipes
        WHERE id = %s AND user_id = %s
        """,
        (id, current_user.id)   # ✅ FIX 2: matches %s %s
    )

    db.commit()
    flash("AI Recipe deleted 🗑️", "success")

    return redirect(url_for("saved.saved_recipes"))