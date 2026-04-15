from flask import Blueprint, redirect, url_for
from flask_login import login_required, current_user
from extensions import db
from models.favorite import SavedRecipe

favorite_bp = Blueprint("favorite", __name__)

@favorite_bp.route("/save/<int:blog_id>")
@login_required
def save_blog(blog_id):
    fav = SavedRecipe.query.filter_by(
        user_id=current_user.id,
        blog_id=blog_id
    ).first()

    if not fav:
        fav = SavedRecipe(user_id=current_user.id, blog_id=blog_id)
        db.session.add(fav)
        db.session.commit()

    return redirect(url_for("blog.blog_detail", slug=blog_id))


@favorite_bp.route("/saved-recipes")
@login_required
def saved_recipes():
    favorites = SavedRecipe.query.filter_by(user_id=current_user.id).all()
    return "Saved Recipes Page"
