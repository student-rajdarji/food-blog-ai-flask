from extensions import db

class SavedRecipe(db.Model):
    __tablename__ = "saved_recipes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    blog_id = db.Column(db.Integer, nullable=False)