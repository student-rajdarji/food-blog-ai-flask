import os
from flask import (
    Blueprint, render_template, redirect,
    url_for, flash, request, abort, current_app
)
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from extensions import db
from models.blog import Blog

blog_bp = Blueprint("blog", __name__, url_prefix="/blogs")


# -----------------------------
# CONFIG
# -----------------------------
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def youtube_to_embed(url):
    """
    Converts watch URLs to embed URLs
    """
    if not url:
        return None

    if "watch?v=" in url:
        return url.replace("watch?v=", "embed/").split("&")[0]

    if "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]
        return f"https://www.youtube.com/embed/{video_id}"

    return url


# -----------------------------
# BLOG LIST (with category filter)
# -----------------------------
@blog_bp.route("/")
def blogs():
    category = request.args.get("category")

    query = Blog.query.filter(Blog.is_featured == False)

    if category:
        query = query.filter(Blog.category == category)

    blogs = query.order_by(Blog.created_at.desc()).all()

    return render_template(
        "blogs/blog_list.html",
        blogs=blogs,
        selected_category=category
    )


# -----------------------------
# BLOG DETAIL
# -----------------------------
@blog_bp.route("/<slug>")
def blog_detail(slug):
    blog = Blog.query.filter_by(slug=slug).first_or_404()
    return render_template("blogs/blog_detail.html", blog=blog)


# -----------------------------
# CREATE BLOG
# -----------------------------
@blog_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_blog():

    if request.method == "POST":
        title = request.form.get("title")
        recipe_name = request.form.get("recipe_name")
        category = request.form.get("category")
        content = request.form.get("content")
        ingredients = request.form.get("ingredients")
        steps = request.form.get("steps")
        serving_info = request.form.get("serving_info")
        nutrition = request.form.get("nutrition")
        tips = request.form.get("tips")
        video_url = youtube_to_embed(request.form.get("video_url"))

        image = request.files.get("image")
        image_path = None

        # 📸 IMAGE UPLOAD
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            upload_folder = os.path.join(current_app.static_folder, "uploads")
            os.makedirs(upload_folder, exist_ok=True)

            image.save(os.path.join(upload_folder, filename))
            image_path = f"uploads/{filename}"

        blog = Blog(
            title=title,
            recipe_name=recipe_name,
            category=category,
            content=content,
            ingredients=ingredients,
            steps=steps,
            serving_info=serving_info,
            nutrition=nutrition,
            tips=tips,
            video_url=video_url,
            image_url=image_path,
            user_id=current_user.id
        )

        db.session.add(blog)
        db.session.commit()

        flash("Blog created successfully 🎉", "success")
        return redirect(url_for("blog.blog_detail", slug=blog.slug))

    return render_template("blogs/create_blog.html")


# -----------------------------
# EDIT BLOG
# -----------------------------
@blog_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_blog(id):
    blog = Blog.query.get_or_404(id)

    if blog.user_id != current_user.id and current_user.username != "raj":
        abort(403)

    if request.method == "POST":
        blog.title = request.form.get("title")
        blog.recipe_name = request.form.get("recipe_name")
        blog.category = request.form.get("category")
        blog.content = request.form.get("content")
        blog.ingredients = request.form.get("ingredients")
        blog.steps = request.form.get("steps")
        blog.serving_info = request.form.get("serving_info")
        blog.nutrition = request.form.get("nutrition")
        blog.tips = request.form.get("tips")
        blog.video_url = youtube_to_embed(request.form.get("video_url"))

        image = request.files.get("image")
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            upload_folder = os.path.join(current_app.static_folder, "uploads")
            os.makedirs(upload_folder, exist_ok=True)

            image.save(os.path.join(upload_folder, filename))
            blog.image_url = f"uploads/{filename}"

        db.session.commit()
        flash("Blog updated successfully ✅", "success")
        return redirect(url_for("blog.blog_detail", slug=blog.slug))

    return render_template("blogs/edit_blog.html", blog=blog)


# -----------------------------
# DELETE BLOG
# -----------------------------
@blog_bp.route("/delete/<int:id>", methods=["POST"])
@login_required
def delete_blog(id):
    blog = Blog.query.get_or_404(id)

    if blog.user_id != current_user.id and current_user.username != "raj":
        abort(403)

    db.session.delete(blog)
    db.session.commit()

    flash("Blog deleted 🗑️", "success")
    return redirect(url_for("blog.blogs"))