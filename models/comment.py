from extensions import db
from datetime import datetime


class Comment(db.Model):

    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True)

    text = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"), nullable=False)

    # Relationships
    user = db.relationship("User", backref="user_comments")

    blog = db.relationship(
        "Blog",
        back_populates="comments"
    )

    