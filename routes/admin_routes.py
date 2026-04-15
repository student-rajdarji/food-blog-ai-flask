from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from extensions import db
from models.blog import Blog
from models.user import User

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/")
@login_required
def dashboard():
    if current_user.username != "raj":
        flash("Unauthorized access", "danger")
        return redirect(url_for("main.home"))

    users = User.query.all()
    blogs = Blog.query.order_by(Blog.id.desc()).all()
    return render_template("admin/dashboard.html", users=users, blogs=blogs)


# 🔥 DELETE BLOG
@admin_bp.route("/delete-blog/<int:blog_id>", methods=["POST"])
@login_required
def delete_blog(blog_id):
    if current_user.username != "raj":
        flash("Unauthorized", "danger")
        return redirect(url_for("main.home"))

    blog = Blog.query.get_or_404(blog_id)
    db.session.delete(blog)
    db.session.commit()

    flash("Blog deleted successfully", "success")
    return redirect(url_for("admin.dashboard"))


# 🔥 DELETE USER
@admin_bp.route("/delete-user/<int:user_id>", methods=["POST"])
@login_required
def delete_user(user_id):
    if current_user.username != "raj":
        flash("Unauthorized", "danger")
        return redirect(url_for("main.home"))

    user = User.query.get_or_404(user_id)

    if user.username == "raj":
        flash("You cannot delete yourself", "warning")
        return redirect(url_for("admin.dashboard"))

    db.session.delete(user)
    db.session.commit()

    flash("User deleted successfully", "success")
    return redirect(url_for("admin.dashboard"))