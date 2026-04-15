import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from models.blog import Blog
from slugify import slugify

blogs = [
    {
        "title": "Classic Indian Breakfast to Start Your Day Right",
        "recipe_name": "Vegetable Poha",
        "category": "Breakfast",
        "excerpt": "Light, quick and healthy Indian breakfast loved by everyone.",
        "content": "Vegetable poha is a popular Indian breakfast made with flattened rice, vegetables and mild spices.",
        "image_url": "images/breakfast_recipe/breakfast1.jpeg",
        "video_url": "https://www.youtube.com/embed/yWkF-2aBDZE",

        "ingredients": """Poha (flattened rice)
Onion
Green peas
Potato
Mustard seeds
Curry leaves
Turmeric
Lemon juice
Salt""",

        "steps": """Wash and soak poha.
Heat oil and add mustard seeds.
Add onion, veggies and spices.
Mix poha well.
Garnish with lemon and serve hot.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 15 mins 🔥 Calories: ~250 kcal",

        "nutrition": """✅ Light on stomach
✅ Rich in carbs
✅ Low fat
✅ Easy to digest""",

        "tips": """Use thin poha
Do not overcook
Add peanuts for crunch"""
    },

    {
        "title": "Healthy South Indian Breakfast Recipe",
        "recipe_name": "Soft Idli with Coconut Chutney",
        "category": "Breakfast",
        "excerpt": "Traditional South Indian breakfast that is soft and nutritious.",
        "content": "Idli is a steamed rice cake served with coconut chutney and sambar.",
        "image_url": "images/breakfast_recipe/breakfast2.jpeg",
        "video_url": "https://www.youtube.com/embed/rC60Y5BtQ8s",

        "ingredients": """Idli batter
Salt
Coconut
Green chili
Roasted chana dal""",

        "steps": """Pour batter into idli moulds.
Steam for 10 minutes.
Prepare chutney by grinding ingredients.
Serve hot.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 20 mins 🔥 Calories: ~180 kcal",

        "nutrition": """✅ Low calorie
✅ Fermented food
✅ Gut friendly
✅ No oil""",

        "tips": """Grease moulds lightly
Use fresh batter
Serve with sambar"""
    },

    {
        "title": "Protein Rich Indian Breakfast Option",
        "recipe_name": "Moong Dal Chilla",
        "category": "Breakfast",
        "excerpt": "High-protein Indian breakfast for fitness lovers.",
        "content": "Moong dal chilla is a healthy Indian pancake made from soaked lentils.",
        "image_url": "images/breakfast_recipe/breakfast3.jpeg",
        "video_url": "https://www.youtube.com/embed/6JXC5N9hF6k",

        "ingredients": """Moong dal
Green chili
Ginger
Cumin seeds
Salt
Oil""",

        "steps": """Soak and grind dal.
Add spices.
Pour batter on pan.
Cook both sides till golden.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 20 mins 🔥 Calories: ~220 kcal",

        "nutrition": """✅ High protein
✅ Low fat
✅ Keeps you full
✅ Muscle friendly""",

        "tips": """Add vegetables in batter
Use non-stick pan
Serve with mint chutney"""
    },

    {
        "title": "Filling Indian Breakfast for Energy",
        "recipe_name": "Aloo Paratha",
        "category": "Breakfast",
        "excerpt": "Popular Indian breakfast loved across India.",
        "content": "Aloo paratha is a stuffed Indian flatbread filled with spiced potatoes.",
        "image_url": "images/breakfast_recipe/breakfast4.jpeg",
        "video_url": "https://www.youtube.com/embed/j1_05wNTUYY",

        "ingredients": """Wheat flour
Boiled potatoes
Green chili
Coriander
Spices
Butter""",

        "steps": """Prepare potato stuffing.
Stuff into dough.
Roll paratha.
Cook on tawa with butter.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 25 mins 🔥 Calories: ~350 kcal",

        "nutrition": """✅ Energy rich
✅ Carb loaded
✅ Satisfying meal
✅ Traditional food""",

        "tips": """Do not overstuff
Serve with curd
Use less butter"""
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
        print("✅ Indian Breakfast blogs seeded successfully")

if __name__ == "__main__":
    run()