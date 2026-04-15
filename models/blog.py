from extensions import db
from datetime import datetime
from slugify import slugify

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)

    recipe_name = db.Column(db.String(100))
    category = db.Column(db.String(50))

    excerpt = db.Column(db.String(500))
    content = db.Column(db.Text, nullable=False)

    ingredients = db.Column(db.Text, default="")
    steps = db.Column(db.Text, default="")
    serving_info = db.Column(db.Text, nullable=True)
    nutrition = db.Column(db.Text, nullable=True)
    tips = db.Column(db.Text, nullable=True)

    image_url = db.Column(db.String(500))
    video_url = db.Column(db.String(500))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_featured = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    author = db.relationship("User", backref="blogs")

      # ✅ FIXED COMMENTS RELATIONSHIP
    comments = db.relationship(
        "Comment",
        back_populates="blog",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.slug:
            self.slug = slugify(self.title)

    def calculate_rating(self):

        if not self.comments:
            return None

        positive_words = [
            "good",
            "great",
            "amazing",
            "delicious",
            "tasty",
            "perfect",
            "excellent",
            "love",
            "best",
            "awesome",
            "nice"
        ]

        negative_words = [
            "bad",
            "worst",
            "bland",
            "boring",
            "poor",
            "terrible",
            "awful",
            "hate"
        ]

        score = 0

        for comment in self.comments:

            text = comment.text.lower()

            for word in positive_words:
                if word in text:
                    score += 1

            for word in negative_words:
                if word in text:
                    score -= 1

        # Convert score to 1-5 rating

        if score >= 2:
            return 5

        elif score == 1:
            return 4

        elif score == 0:
            return 3

        elif score == -1:
            return 2

        else:
            return 1

    # ================= OPTIONAL: GET STAR STRING =================

    def get_star_rating(self):

        rating = self.calculate_rating()

        if not rating:
            return "No rating yet"

        return "⭐" * rating + "☆" * (5 - rating)

    # ================= DEBUG STRING =================

    def _repr_(self):

        return f"<Blog {self.title}>"