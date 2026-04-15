from extensions import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    steps = db.Column(db.Text, nullable=False)
    time_required = db.Column(db.String(50))
    servings = db.Column(db.String(20))
    image = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    category_id=db.Column(db.Integer,db.ForeignKey('category.id'))
