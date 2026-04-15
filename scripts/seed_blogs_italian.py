import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from models.blog import Blog
from slugify import slugify

blogs = [
    {
        "title": "Classic Italian Pasta for Dinner",
        "recipe_name": "Creamy Alfredo Pasta",
        "category": "Italian",
        "excerpt": "Rich and creamy Italian-style pasta for comfort dinners.",
        "content": "A classic Italian Alfredo pasta made with creamy sauce and herbs.",
        "image_url": "images/italian/italian1.jpeg",
        "video_url": "https://www.youtube.com/embed/9n5z0LTGII4",

        "ingredients": """Pasta
Butter
Garlic
Fresh cream
Parmesan cheese
Italian herbs
Salt & pepper""",

        "steps": """Boil pasta until al dente.
Melt butter and sauté garlic.
Add cream and cheese.
Mix pasta with sauce and serve hot.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 20 mins 🔥 Calories: ~450 kcal",

        "nutrition": """✅ Rich in calcium
✅ Energy boosting
✅ Comfort food
✅ Protein rich""",

        "tips": """Add mushrooms for extra flavor
Use whole wheat pasta
Top with chili flakes"""
    },

    {
        "title": "Authentic Italian Pizza at Home",
        "recipe_name": "Margherita Pizza",
        "category": "Italian",
        "excerpt": "Traditional Italian pizza with fresh basil and mozzarella.",
        "content": "A simple yet iconic Italian pizza loved worldwide.",
        "image_url": "images/italian/italian2.jpeg",
        "video_url": "https://www.youtube.com/embed/xKDnD8sJsuY",

        "ingredients": """Pizza base
Tomato sauce
Mozzarella cheese
Fresh basil
Olive oil
Salt""",

        "steps": """Spread sauce on pizza base.
Add mozzarella evenly.
Bake until crust is golden.
Garnish with basil and olive oil.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 25 mins 🔥 Calories: ~500 kcal",

        "nutrition": """✅ Good source of calcium
✅ Balanced carbs
✅ Fresh ingredients
✅ Light yet filling""",

        "tips": """Use fresh mozzarella
Bake on high temperature
Add cherry tomatoes"""
    },

    {
        "title": "Light Italian Soup for Evenings",
        "recipe_name": "Classic Minestrone Soup",
        "category": "Italian",
        "excerpt": "A healthy Italian vegetable soup perfect for light meals.",
        "content": "Traditional Italian soup loaded with vegetables and beans.",
        "image_url": "images/italian/italian3.jpeg",
        "video_url": "https://www.youtube.com/embed/GdcCVZ_D7hQ",

        "ingredients": """Carrots
Beans
Tomatoes
Onion
Garlic
Pasta
Italian herbs""",

        "steps": """Sauté vegetables lightly.
Add water and tomatoes.
Add beans and pasta.
Simmer and serve warm.""",

        "serving_info": "🍽 Serves 3 ⏱ Prep time: 30 mins 🔥 Calories: ~220 kcal",

        "nutrition": """✅ High fiber
✅ Low calorie
✅ Heart healthy
✅ Immunity boosting""",

        "tips": """Add zucchini for flavor
Use vegetable stock
Serve with garlic bread"""
    },

    {
        "title": "Italian Dessert for Sweet Lovers",
        "recipe_name": "Classic Tiramisu",
        "category": "Italian",
        "excerpt": "Famous Italian dessert with coffee and mascarpone.",
        "content": "A rich and creamy Italian dessert layered with coffee flavor.",
        "image_url": "images/italian/italian4.jpeg",
        "video_url": "https://www.youtube.com/embed/x5E70W40KNI",

        "ingredients": """Ladyfinger biscuits
Mascarpone cheese
Coffee
Cocoa powder
Sugar
Cream""",

        "steps": """Dip biscuits in coffee.
Layer with mascarpone cream.
Repeat layers.
Chill and dust cocoa powder.""",

        "serving_info": "🍽 Serves 4 ⏱ Prep time: 25 mins 🔥 Calories: ~380 kcal",

        "nutrition": """✅ Energy rich
✅ Calcium source
✅ Mood boosting
✅ Perfect dessert""",

        "tips": """Chill overnight for best taste
Use dark cocoa powder
Serve cold"""
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
                blog = Blog(
                    title=b["title"],
                    slug=slug,
                    excerpt=b["excerpt"],
                    content=b["content"],
                    image_url=b["image_url"],
                    category=b["category"],
                    recipe_name=b["recipe_name"],
                    video_url=b["video_url"],
                    ingredients=b["ingredients"],
                    steps=b["steps"],
                    serving_info=b["serving_info"],
                    nutrition=b["nutrition"],
                    tips=b["tips"]
                )
                db.session.add(blog)

        db.session.commit()
        print("✅ Italian blogs seeded successfully")

if __name__ == "__main__":
    run()