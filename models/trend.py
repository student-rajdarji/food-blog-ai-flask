from extensions import db

class Trend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.String(100), unique=True, nullable=False)
