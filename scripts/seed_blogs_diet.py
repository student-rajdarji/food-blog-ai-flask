import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from models.blog import Blog
from slugify import slugify

blogs = [
    {
        "title": "Low Calorie Diet Breakfast Ideas",
        "recipe_name": "Veg Oats Porridge",
        "category": "Diet",
        "excerpt": "Light and filling breakfast ideas for weight loss.",
        "content": "A warm, low-calorie oats porridge loaded with vegetables to keep you full longer.",
        "image_url": "images/diet/diet1.jpeg",
        "video_url": "https://www.youtube.com/embed/3dyy1SyKwCE",

        "ingredients": """Rolled oats
Carrot (grated)
Beans
Water
Salt
Black pepper""",

        "steps": """Boil oats in water.
Add vegetables and cook well.
Season with salt and pepper.
Serve hot.""",

        "serving_info": "🍽 Serves 1 ⏱ Prep time: 10 mins 🔥 Calories: ~180 kcal",

        "nutrition": """✅Low calorie
✅High fiber
✅Keeps you full
✅ Aids weight loss""",

        "tips": """Avoid milk for fewer calories
Add flax seeds for fiber
Use minimal salt"""
    },

    {
        "title": "Healthy Diet Lunch for Weight Loss",
        "recipe_name": "Grilled Veggie Salad",
        "category": "Diet",
        "excerpt": "Simple diet-friendly lunch recipes.",
        "content": "A fresh and light grilled vegetable salad with minimal oil.",
        "image_url": "images/diet/diet2.jpeg",
        "video_url": "https://www.youtube.com/embed/CjTPBlW3gMA",

        "ingredients": """Bell peppers
Zucchini
Broccoli
Olive oil (1 tsp)
Lemon juice
Salt""",

        "steps": """Grill vegetables lightly.
Mix with lemon juice.
Add olive oil and salt.
Serve fresh.""",

        "serving_info": "🍽 Serves 1 ⏱ Prep time: 15 mins 🔥 Calories: ~220 kcal",

        "nutrition": """✅Low fat
✅High vitamins
✅Improves digestion
✅ Heart healthy""",

        "tips": """Avoid heavy dressings
Add lettuce for volume
Use air fryer for grilling"""
    },

    {
        "title": "Evening Diet Snacks Under 200 Calories",
        "recipe_name": "Sprout Chaat",
        "category": "Diet",
        "excerpt": "Healthy evening snacks for dieting.",
        "content": "A protein-rich sprout chaat to curb evening hunger.",
        "image_url": "images/diet/diet3.jpeg",
        "video_url": "https://www.youtube.com/embed/K843BPF6OV0",

        "ingredients": """Boiled sprouts
Onion (finely chopped)
Tomato
Lemon juice
Salt
Chaat masala""",

        "steps": """Mix all ingredients.
Add lemon juice and spices.
Toss well.
Serve immediately.""",

        "serving_info": "🍽 Serves 1 ⏱ Prep time: 5 mins 🔥 Calories: ~150 kcal",

        "nutrition": """✅High protein
✅Low calorie
✅Boosts metabolism
✅ Keeps hunger away""",

        "tips": """Skip potatoes
Add cucumber for crunch
Use less salt"""
    },

    {
        "title": "Light Diet Dinner Recipes",
        "recipe_name": "Vegetable Clear Soup",
        "category": "Diet",
        "excerpt": "Light dinner recipes for weight loss.",
        "content": "A comforting clear soup ideal for a light and healthy dinner.",
        "image_url": "images/diet/diet4.jpeg",
        "video_url": "https://www.youtube.com/embed/V6i2huxK_OQ",

        "ingredients": """Carrot
Cabbage
Beans
Garlic
Water
Salt & pepper""",

        "steps": """Boil vegetables in water.
Add garlic and seasoning.
Simmer for 10 minutes.
Serve warm.""",

        "serving_info": "🍽 Serves 1 ⏱ Prep time: 15 mins 🔥 Calories: ~120 kcal",

        "nutrition": """✅Very low calorie
✅Easy to digest
✅ Hydrating
✅ Weight loss friendly""",

        "tips": """Avoid cornflour
Do not add butter
Add herbs for flavor"""
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
        print("✅ Diet blogs seeded successfully")

if __name__ == "__main__":
    run()