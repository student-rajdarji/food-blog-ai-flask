from flask import Blueprint, render_template

category_bp = Blueprint("category", __name__)

@category_bp.route("/categories")
def categories():
    return render_template("categories.html")