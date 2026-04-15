import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from models.blog import Blog
from slugify import slugify

blogs = [
    {
        "title": "High Protein Breakfast for Muscle Gain",
        "recipe_name": "Paneer Veg Bhurji",
        "category": "High Protein",
        "excerpt": "A protein-rich breakfast ideal for muscle building.",
        "content": "Paneer Veg Bhurji is a quick and delicious Indian breakfast loaded with protein.",
        "image_url": "images/high_protien/protien1.jpeg",
        "video_url": "https://www.youtube.com/embed/KgW--wj5iBM",

        "ingredients": """Paneer (crumbled)
Onion (chopped)
Tomato (chopped)
Capsicum
Green chili
Turmeric
Red chili powder
Salt
Oil""",

        "steps": """Heat oil in a pan.
Sauté onion and chili.
Add tomato and spices.
Add crumbled paneer.
Cook for 5 minutes and serve hot.""",

        "serving_info": "🍽 Serves 1 ⏱ Prep Time: 10 mins 🔥 Protein: ~25g",

        "nutrition": """✅ High protein
✅ Low carb
✅ Muscle friendly
✅ Keeps you full""",

        "tips": """Use low-fat paneer for dieting
Add spinach for extra nutrition
Serve with whole wheat toast"""
    },

    {
        "title": "Protein Packed Lunch Bowl",
        "recipe_name": "Rajma Quinoa Power Bowl",
        "category": "High Protein",
        "excerpt": "A wholesome protein-rich lunch bowl.",
        "content": "Rajma Quinoa Bowl combines plant protein and fiber for a filling lunch.",
        "image_url": "images/high_protien/protien2.jpeg",
        "video_url": "https://www.youtube.com/embed/d7zEp06mH58",

        "ingredients": """Cooked quinoa
Boiled rajma
Onion
Tomato
Cumin
Olive oil
Salt""",

        "steps": """Heat oil and add cumin.
Add onion and tomato.
Add rajma and spices.
Mix with cooked quinoa and serve.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep Time: 20 mins 🔥 Protein: ~22g",

        "nutrition": """✅ Plant-based protein
✅ High fiber
✅ Heart healthy
✅ Energy boosting""",

        "tips": """Add avocado for healthy fats
Use brown rice instead of quinoa
Add lemon juice for freshness"""
    },

    {
        "title": "High Protein Evening Snack",
        "recipe_name": "Moong Dal Chilla with Curd Dip",
        "category": "High Protein",
        "excerpt": "A healthy and filling protein snack.",
        "content": "Moong Dal Chilla is light, nutritious and perfect for evening hunger.",
        "image_url": "images/high_protien/protien3.jpeg",
        "video_url": "https://www.youtube.com/embed/6JXC5N9hF6k",

        "ingredients": """Soaked moong dal
Ginger
Green chili
Salt
Oil
Curd""",

        "steps": """Grind soaked dal to batter.
Add spices.
Cook chilla on pan.
Serve with curd dip.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep Time: 15 mins 🔥 Protein: ~18g",

        "nutrition": """✅ High protein
✅ Easy digestion
✅ Low fat
✅ Diabetic friendly""",

        "tips": """Use non-stick pan to reduce oil
Add grated carrot
Serve with mint chutney"""
    },

    {
        "title": "High Protein Dinner for Weight Loss",
        "recipe_name": "Grilled Chicken with Stir-Fry Veggies",
        "category": "High Protein",
        "excerpt": "Lean protein dinner ideal for weight loss.",
        "content": "Grilled chicken paired with veggies makes a perfect low-carb dinner.",
        "image_url": "images/high_protien/protien4.jpeg",
        "video_url": "https://www.youtube.com/embed/5dybdeTylz0",

        "ingredients": """Chicken breast
Bell peppers
Broccoli
Garlic
Olive oil
Salt
Pepper""",

        "steps": """Marinate chicken with spices.
Grill until cooked.
Stir-fry veggies lightly.
Serve together hot.""",

        "serving_info": "🍽 Serves 1 ⏱ Prep Time: 25 mins 🔥 Protein: ~35g",

        "nutrition": """✅ Very high protein
✅ Low carb
✅ Weight loss friendly
✅ Muscle recovery""",

        "tips": """Use air fryer instead of grill
Replace chicken with tofu for veg version
Add chili flakes for spice"""
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
        print("✅ High Protein blogs seeded successfully")

if __name__ == "__main__":
    run()