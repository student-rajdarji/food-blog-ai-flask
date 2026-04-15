from flask import Blueprint, redirect, url_for, flash, request
from flask_login import login_required, current_user
from db import db

save_bp = Blueprint("save", __name__)

@save_bp.route("/save/<int:blog_id>", methods=["POST"])
@login_required
def save_recipe(blog_id):
    cursor = db.cursor(dictionary=True)

    # Check blog exists
    cursor.execute("SELECT id FROM blog WHERE id=%s", (blog_id,))
    blog = cursor.fetchone()
    if not blog:
        flash("Recipe not found", "danger")
        return redirect("/blogs")

    # Prevent duplicate save
    cursor.execute("""
        SELECT id FROM saved_recipes
        WHERE user_id=%s AND blog_id=%s
    """, (current_user.id, blog_id))

    if cursor.fetchone():
        flash("Already saved ❤️", "info")
        return redirect(request.referrer)

    # Save relation
    cursor.execute("""
        INSERT INTO saved_recipes (user_id, blog_id)
        VALUES (%s, %s)
    """, (current_user.id, blog_id))

    db.commit()
    flash("Recipe saved ❤️", "success")
    return redirect(request.referrer)