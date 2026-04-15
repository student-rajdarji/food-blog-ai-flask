from extensions import db
from datetime import datetime

class AIRecipe(db.Model):
    __tablename__ = "saved_ai_recipes"   # 👈 IMPORTANT: match your real table name

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    recipe = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)