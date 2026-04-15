import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from models.blog import Blog
from slugify import slugify

blogs = [
    {
        "title": "Quick Veg Cheese Sandwich",
        "recipe_name": "Cheese Veg Grilled Sandwich",
        "category": "Quick & Easy",
        "excerpt": "A quick and crispy veg cheese sandwich ready in minutes.",
        "content": "This veg cheese sandwich is perfect for busy mornings or evening hunger.",
        "image_url": "images/quick_easy/quick1.jpeg",
        "video_url": "https://www.youtube.com/embed/4EtrrCP02g8",

        "ingredients": """Bread slices
Grated cheese
Onion (chopped)
Capsicum (chopped)
Butter
Salt & pepper""",

        "steps": """Butter the bread slices.
Add veggies and cheese.
Grill until golden and crispy.
Serve hot.""",

        "serving_info": "🍽 Serves 1 ⏱ Prep time: 10 mins 🔥 Calories: ~320 kcal",

        "nutrition": """✅Quick energy
✅Calcium rich
✅Good for snacks""",

        "tips": """Use brown bread for healthier option
Add chili flakes for spice
Use cheese slice if short on time"""
    },

    {
        "title": "Instant Masala Maggi",
        "recipe_name": "5-Minute Spicy Maggi",
        "category": "Quick & Easy",
        "excerpt": "Classic masala Maggi made instantly with extra flavor.",
        "content": "A quick comfort food loved by all age groups.",
        "image_url": "images/quick_easy/quick2.jpeg",
        "video_url": "https://www.youtube.com/embed/HZno_fFusw0",

        "ingredients": """Maggi noodles
Maggi masala
Water
Chopped onion
Green chili (optional)""",

        "steps": """Boil water.
Add noodles and masala.
Cook for 2–3 minutes.
Serve hot.""",

        "serving_info": "🍽 Serves 1 ⏱ Prep time: 5 mins 🔥 Calories: ~290 kcal",

        "nutrition": """✅Instant meal
✅Filling
✅Comfort food""",

        "tips": """Add veggies to make it healthier
Top with cheese for fusion taste"""
    },

    {
        "title": "Quick Paneer Stir Fry",
        "recipe_name": "Spicy Paneer Toss",
        "category": "Quick & Easy",
        "excerpt": "A protein-rich paneer stir fry ready in under 15 minutes.",
        "content": "Perfect quick dinner or lunch box recipe.",
        "image_url": "images/quick_easy/quick3.jpeg",
        "video_url": "https://www.youtube.com/embed/uQNQSqqB6E0",

        "ingredients": """Paneer cubes
Capsicum
Onion
Soy sauce
Oil
Pepper""",

        "steps": """Heat oil in a pan.
Add paneer and veggies.
Toss with sauces.
Serve hot.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 15 mins 🔥 Calories: ~360 kcal",

        "nutrition": """✅High protein
✅Low carb
✅Keeps you full""",

        "tips": """Use tofu for vegan option
Add chili sauce for extra spice"""
    },

    {
        "title": "Eggless Chocolate Mug Cake",
        "recipe_name": "5-Minute Mug Cake",
        "category": "Quick & Easy",
        "excerpt": "Instant chocolate mug cake made in microwave.",
        "content": "A quick dessert when sweet cravings hit.",
        "image_url": "images/quick_easy/quick4.jpeg",
        "video_url": "https://www.youtube.com/embed/aAjzyBEMqiw",

        "ingredients": """All-purpose flour
Cocoa powder
Sugar
Milk
Oil
Baking powder""",

        "steps": """Mix all ingredients in a mug.
Microwave for 2 minutes.
Let it cool slightly.
Enjoy directly.""",

        "serving_info": "🍽 Serves 1 ⏱ Prep time: 5 mins 🔥 Calories: ~350 kcal",

        "nutrition": """✅Instant dessert
✅Mood booster
✅Quick energy""",

        "tips": """Add choco chips for richness
Serve with ice cream"""
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
        print("✅ Quick & Easy blogs seeded successfully")

if __name__ == "__main__":
    run()