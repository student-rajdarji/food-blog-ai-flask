import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from models.blog import Blog
from slugify import slugify

blogs = [

    {
        "title": "Classic Veg Cheese Burger",
        "recipe_name": "Cheesy Veg Burger",
        "category": "Fast Food",
        "excerpt": "A classic fast food veg burger loaded with cheese and fresh veggies.",
        "content": "This veg cheese burger is crispy, cheesy, and perfect for fast food lovers.",
        "image_url": "images/fast_food/fastfood1.jpeg",
        "video_url": "https://www.youtube.com/embed/X5Eny11uM9o",

        "ingredients": """Burger buns
Veg patty
Cheese slice
Onion slices
Tomato slices
Lettuce
Butter
Mayonnaise""",

        "steps": """Toast burger buns with butter.
Cook veg patty until crispy.
Place patty on bun.
Add cheese and vegetables.
Cover with top bun and serve hot.""",

        "serving_info": "🍽 Serves 1 ⏱ Prep time: 15 mins 🔥 Calories: ~450 kcal",

        "nutrition": """✅Quick energy
✅Good source of carbs
✅Calcium from cheese
⚠ High in calories""",

        "tips": """Use whole wheat buns for healthier option
Add jalapenos for spice
Use homemade patties"""
    },

    {
        "title": "Crispy French Fries at Home",
        "recipe_name": "Golden French Fries",
        "category": "Fast Food",
        "excerpt": "Perfectly crispy french fries made easily at home.",
        "content": "These homemade french fries are crispy on the outside and soft inside.",
        "image_url": "images/fast_food/fastfood2.jpeg",
        "video_url": "https://www.youtube.com/embed/lB8dMNj7JMA",

        "ingredients": """Potatoes
Salt
Cornflour
Oil for frying
Chili powder""",

        "steps": """Peel and cut potatoes.
Soak in cold water for 30 minutes.
Dry and coat with cornflour.
Deep fry until golden.
Sprinkle salt and spices.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 20 mins 🔥 Calories: ~350 kcal",

        "nutrition": """✅High energy
✅Carb rich
⚠ High fat
⚠ Not ideal for daily consumption""",

        "tips": """Air fry for low oil version
Serve with peri peri seasoning
Double fry for extra crispiness"""
    },

    {
        "title": "Cheesy Veg Pizza",
        "recipe_name": "Homemade Veg Pizza",
        "category": "Fast Food",
        "excerpt": "A delicious homemade pizza loaded with veggies and cheese.",
        "content": "This veg pizza is perfect for weekend cravings and family dinners.",
        "image_url": "images/fast_food/fastfood3.jpeg",
        "video_url": "https://www.youtube.com/embed/kSb62MGJSI4",

        "ingredients": """Pizza base
Pizza sauce
Mozzarella cheese
Capsicum
Onion
Sweet corn
Oregano""",

        "steps": """Preheat oven.
Spread sauce on pizza base.
Add vegetables and cheese.
Bake until cheese melts.
Sprinkle oregano and serve.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 25 mins 🔥 Calories: ~600 kcal",

        "nutrition": """✅High calcium
✅Energy rich
⚠ High calories
⚠ High sodium""",

        "tips": """Use whole wheat base
Add olives or jalapenos
Control cheese for lighter version"""
    },

    {
        "title": "Street Style Veg Momos",
        "recipe_name": "Steamed Veg Momos",
        "category": "Fast Food",
        "excerpt": "Popular street-style momos made at home.",
        "content": "Soft dumplings stuffed with spicy vegetable filling served with chutney.",
        "image_url": "images/fast_food/fastfood4.jpeg",
        "video_url": "https://www.youtube.com/embed/kfvXn1RMRpY",

        "ingredients": """All purpose flour
Cabbage
Carrot
Capsicum
Garlic
Soy sauce
Salt & pepper""",

        "steps": """Prepare dough and rest it.
Make vegetable stuffing.
Fill and shape momos.
Steam for 10 minutes.
Serve hot with chutney.""",

        "serving_info": "🍽 Serves 3 ⏱ Prep time: 30 mins 🔥 Calories: ~300 kcal",

        "nutrition": """✅Steamed & low fat
✅Veg loaded
⚠ Refined flour
⚠ Sodium from sauces""",

        "tips": """Use wheat flour for healthier momos
Pan fry for crispy version
Add paneer for richness"""
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
        print("✅ Fast Food blogs seeded successfully")

if __name__ == "__main__":
    run()