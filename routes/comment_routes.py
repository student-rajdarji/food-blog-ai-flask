from flask import Blueprint, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user

from extensions import db
from models.comment import Comment
from models.blog import Blog

comment_bp = Blueprint("comment", __name__, url_prefix="/comments")


# ================= ADD COMMENT =================
@comment_bp.route("/add/<int:blog_id>", methods=["POST"])
@login_required
def add_comment(blog_id):

    blog = Blog.query.get_or_404(blog_id)

    text = request.form.get("text")

    if not text or text.strip() == "":
        flash("Comment cannot be empty", "danger")
        return redirect(url_for("blog.blog_detail", slug=blog.slug))

    comment = Comment(
        text=text,
        user_id=current_user.id,
        blog_id=blog.id
    )

    db.session.add(comment)
    db.session.commit()

    flash("Comment added successfully 💬", "success")

    return redirect(url_for("blog.blog_detail", slug=blog.slug))


# ================= DELETE COMMENT =================
@comment_bp.route("/delete/<int:comment_id>", methods=["POST"])
@login_required
def delete_comment(comment_id):

    comment = Comment.query.get_or_404(comment_id)

    if (
        comment.user_id != current_user.id
        and comment.blog.user_id != current_user.id
        and current_user.username != "raj"
    ):
        abort(403)

    slug = comment.blog.slug

    db.session.delete(comment)
    db.session.commit()

    flash("Comment deleted 🗑️", "success")

    return redirect(url_for("blog.blog_detail", slug=slug))