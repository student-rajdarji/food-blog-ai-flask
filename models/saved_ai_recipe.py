from datetime import datetime
from extensions import db

class SavedAIRecipe(db.Model):
    __tablename__ = "saved_ai_recipes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True)
    title = db.Column(db.String(255), nullable=False)
    recipe = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)