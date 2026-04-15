import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from models.blog import Blog
from slugify import slugify

blogs = [

    # 1️⃣ VEGAN BREAKFAST
    {
        "title": "High-Energy Vegan Breakfast Ideas",
        "recipe_name": "Peanut Butter Banana Toast",
        "category": "Vegan",
        "excerpt": "Quick and energy-boosting vegan breakfast recipes.",
        "content": "A simple yet powerful vegan breakfast loaded with healthy fats and fiber.",
        "image_url": "images/vegan/vegan1.jpeg",
        "video_url": "https://www.youtube.com/embed/Le5DpqvALHQ",

        "ingredients": """Whole wheat bread
Peanut butter
Banana slices
Chia seeds""",

        "steps": """Toast the bread slices.
Spread peanut butter evenly.
Top with banana slices.
Sprinkle chia seeds and serve.""",

        "serving_info": "🍽 Serves 1 ⏱ Prep time: 5 mins 🔥 Calories: ~300 kcal",

        "nutrition": """✅ Healthy fats
✅ High energy
✅ Plant-based protein
✅ Heart healthy""",

        "tips": """Use almond butter as alternative
Add cocoa nibs for flavor
Use multigrain bread"""
    },

    # 2️⃣ VEGAN LUNCH
    {
        "title": "Filling Vegan Lunch Bowl Recipes",
        "recipe_name": "Chickpea Buddha Bowl",
        "category": "Vegan",
        "excerpt": "Wholesome vegan lunch bowls packed with nutrition.",
        "content": "A colorful chickpea buddha bowl rich in protein and fiber.",
        "image_url": "images/vegan/vegan2.jpeg",
        "video_url": "https://www.youtube.com/embed/agMMtecXnb8",

        "ingredients": """Boiled chickpeas
Cooked quinoa
Cucumber
Carrot
Tahini sauce""",

        "steps": """Roast chickpeas with spices.
Arrange quinoa and vegetables in a bowl.
Add roasted chickpeas.
Drizzle tahini sauce.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 20 mins 🔥 Calories: ~420 kcal",

        "nutrition": """✅ High protein
✅ Rich in fiber
✅ Balanced macros
✅ Keeps you full""",

        "tips": """Add avocado slices
Use hummus instead of tahini
Sprinkle sesame seeds"""
    },

    # 3️⃣ VEGAN SNACK
    {
        "title": "Crispy Vegan Evening Snacks",
        "recipe_name": "Vegan Sweet Potato Fries",
        "category": "Vegan",
        "excerpt": "Crispy and guilt-free vegan snack ideas.",
        "content": "Baked sweet potato fries that are crispy outside and soft inside.",
        "image_url": "images/vegan/vegan3.jpeg",
        "video_url": "https://www.youtube.com/embed/42ySS8yd7QU",

        "ingredients": """Sweet potatoes
Olive oil
Paprika
Garlic powder
Salt""",

        "steps": """Cut sweet potatoes into strips.
Toss with oil and spices.
Bake until crispy.
Serve hot.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 25 mins 🔥 Calories: ~260 kcal",

        "nutrition": """✅ Rich in antioxidants
✅ Low fat
✅ High fiber
✅ Good for digestion""",

        "tips": """Air-fry for extra crispiness
Serve with vegan mayo
Add chili flakes"""
    },

    # 4️⃣ VEGAN DINNER
    {
        "title": "Comforting Vegan Dinner Recipes",
        "recipe_name": "Vegan Lentil Curry",
        "category": "Vegan",
        "excerpt": "Comforting and protein-rich vegan dinner recipes.",
        "content": "A warm lentil curry cooked with Indian spices and herbs.",
        "image_url": "images/vegan/vegan4.jpeg",
        "video_url": "https://www.youtube.com/embed/V997_6De0tA",

        "ingredients": """Red lentils
Onion
Tomato
Garlic
Ginger
Indian spices""",

        "steps": """Cook lentils until soft.
Sauté onion, garlic, and ginger.
Add tomatoes and spices.
Mix lentils and simmer.""",

        "serving_info": "🍽 Serves 3 ⏱ Prep time: 30 mins 🔥 Calories: ~380 kcal",

        "nutrition": """✅ High protein
✅ Iron rich
✅ Vegan comfort food
✅ Gut friendly""",

        "tips": """Serve with rice or roti
Add coconut milk for creaminess
Garnish with coriander"""
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
        print("✅ Vegan blogs added/updated successfully")

if __name__ == "__main__":
    run()