import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from models.blog import Blog
from slugify import slugify

blogs = [

    {
        "title": "Rich Chocolate Fudge Brownie",
        "recipe_name": "Chocolate Fudge Brownie",
        "category": "Dessert",
        "excerpt": "Soft, gooey and rich chocolate brownies for dessert lovers.",
        "content": "These chocolate fudge brownies are rich, moist and melt-in-mouth perfect for any occasion.",
        "image_url": "images/dessert/dessert1.jpeg",
        "video_url": "https://www.youtube.com/embed/X9hKRIQ3uxc",

        "ingredients": """Dark chocolate
Butter
Sugar
Eggs
All-purpose flour
Cocoa powder""",

        "steps": """Melt chocolate and butter together.
Mix sugar and eggs.
Fold in dry ingredients.
Bake until fudgy and soft.""",

        "serving_info": "🍽 Serves 6 ⏱ Prep time: 40 mins 🔥 Calories: ~320 kcal",

        "nutrition": """✅ Rich in antioxidants
✅ Energy boosting
✅ Mood enhancer""",

        "tips": """Do not overbake
Use dark chocolate for best taste
Serve with vanilla ice cream"""
    },

    {
        "title": "Classic Homemade Vanilla Ice Cream",
        "recipe_name": "Vanilla Ice Cream",
        "category": "Dessert",
        "excerpt": "Creamy and smooth homemade vanilla ice cream.",
        "content": "A simple and creamy vanilla ice cream made with basic ingredients at home.",
        "image_url": "images/dessert/dessert2.jpeg",
        "video_url": "https://www.youtube.com/embed/PI6Rbxkr9V0",

        "ingredients": """Fresh cream
Milk
Sugar
Vanilla essence""",

        "steps": """Whip cream until fluffy.
Mix milk, sugar and vanilla.
Freeze and whisk twice.
Serve chilled.""",

        "serving_info": "🍽 Serves 4 ⏱ Prep time: 6 hrs 🔥 Calories: ~210 kcal",

        "nutrition": """✅ Calcium rich
✅ Good energy source
✅ Homemade & preservative-free""",

        "tips": """Add chocolate chips
Use condensed milk for richness
Serve with brownies"""
    },

    {
        "title": "Traditional Gulab Jamun Delight",
        "recipe_name": "Gulab Jamun",
        "category": "Dessert",
        "excerpt": "Soft and juicy gulab jamuns soaked in sugar syrup.",
        "content": "Classic Indian dessert made with khoya and soaked in aromatic sugar syrup.",
        "image_url": "images/dessert/dessert3.jpeg",
        "video_url": "https://www.youtube.com/embed/QFvd7u_YjVk",

        "ingredients": """Khoya
Maida
Milk
Sugar
Cardamom
Rose water""",

        "steps": """Prepare dough with khoya.
Shape small balls.
Fry on low flame.
Soak in warm sugar syrup.""",

        "serving_info": "🍽 Serves 8 ⏱ Prep time: 45 mins 🔥 Calories: ~180 kcal",

        "nutrition": """✅ Instant energy
✅ Rich festive dessert
✅ Calcium source""",

        "tips": """Fry on low flame only
Do not overcrowd pan
Serve warm"""
    },

    {
        "title": "No-Bake Mango Cheesecake",
        "recipe_name": "Mango Cheesecake",
        "category": "Dessert",
        "excerpt": "Creamy mango cheesecake without baking.",
        "content": "A refreshing mango cheesecake perfect for summer desserts.",
        "image_url": "images/dessert/dessert4.jpeg",
        "video_url": "https://www.youtube.com/embed/WINcAAFPzB4",

        "ingredients": """Cream cheese
Fresh mango pulp
Digestive biscuits
Butter
Sugar""",

        "steps": """Prepare biscuit base.
Whip cream cheese and mango pulp.
Pour over base.
Chill for 4 hours.""",

        "serving_info": "🍽 Serves 6 ⏱ Prep time: 4 hrs 🔥 Calories: ~260 kcal",

        "nutrition": """✅ Vitamin A rich
✅ Calcium source
✅ Refreshing dessert""",

        "tips": """Use ripe mangoes
Chill overnight for best texture
Top with mango cubes"""
    }

]

def run():
    app = create_app()
    with app.app_context():
        for b in blogs:
            slug = slugify(b["title"])
            blog = Blog.query.filter_by(slug=slug).first()

            if blog:
                for key, value in b.items():
                    setattr(blog, key, value)
            else:
                blog = Blog(**b, slug=slug)
                db.session.add(blog)

        db.session.commit()
        print("✅ Dessert blogs seeded successfully")

if __name__ == "__main__":
    run()