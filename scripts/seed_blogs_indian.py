import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from models.blog import Blog
from slugify import slugify

blogs = [

    {
        "title": "Rich Paneer Butter Masala",
        "recipe_name": "Paneer Butter Masala",
        "category": "Indian",
        "excerpt": "Creamy and mildly spiced paneer curry loved across India.",
        "content": "Paneer butter masala is a rich tomato-based curry made with soft paneer cubes and aromatic spices.",
        "image_url": "images/indian/indian1.jpeg",
        "video_url": "https://www.youtube.com/embed/oYZ--rdHL6I",

        "ingredients": """Paneer cubes
Tomatoes
Butter
Cream
Ginger garlic paste
Red chili powder
Garam masala
Kasuri methi
Salt""",

        "steps": """Heat butter in pan.
Add ginger garlic paste and tomatoes.
Cook till thick gravy forms.
Add spices and paneer.
Finish with cream and kasuri methi.""",

        "serving_info": "🍽 Serves 2–3 ⏱ Prep time: 30 mins 🔥 Calories: ~450 kcal",

        "nutrition": """✅High protein
✅Calcium rich
✅Energy dense
✅Good for weight gain""",

        "tips": """Use fresh paneer
Do not overcook paneer
Adjust cream as per taste"""
    },

    {
        "title": "Fragrant Vegetable Biryani",
        "recipe_name": "Veg Dum Biryani",
        "category": "Indian",
        "excerpt": "Aromatic rice dish layered with spiced vegetables.",
        "content": "Vegetable biryani is a classic Indian rice dish cooked with basmati rice, spices and vegetables.",
        "image_url": "images/indian/indian2.jpeg",
        "video_url": "https://www.youtube.com/embed/m-hO_lpj0h0",

        "ingredients": """Basmati rice
Mixed vegetables
Onion
Yogurt
Ginger garlic paste
Biryani masala
Mint leaves
Saffron milk""",

        "steps": """Cook rice till 70%.
Prepare vegetable masala.
Layer rice and vegetables.
Cover and cook on low flame.
Serve hot with raita.""",

        "serving_info": "🍽 Serves 3 ⏱ Prep time: 40 mins 🔥 Calories: ~520 kcal",

        "nutrition": """✅Balanced carbs
✅Fiber rich
✅Filling meal
✅Good energy source""",

        "tips": """Use long grain rice
Cook on dum for best flavor
Add fried onions for aroma"""
    },

    {
        "title": "Punjabi Style Chole Masala",
        "recipe_name": "Chole Masala",
        "category": "Indian",
        "excerpt": "Spicy chickpea curry popular in North India.",
        "content": "Chole masala is a hearty Indian curry made using chickpeas cooked in bold spices.",
        "image_url": "images/indian/indian3.jpeg",
        "video_url": "https://www.youtube.com/embed/M-ohmJswy6A",

        "ingredients": """Boiled chickpeas
Onion
Tomatoes
Ginger garlic paste
Chole masala
Cumin seeds
Oil
Salt""",

        "steps": """Heat oil and add cumin seeds.
Add onions and sauté.
Add tomatoes and spices.
Add chickpeas and cook well.
Serve with roti or rice.""",

        "serving_info": "🍽 Serves 3 ⏱ Prep time: 35 mins 🔥 Calories: ~400 kcal",

        "nutrition": """✅High protein
✅High fiber
✅Plant based
✅Heart healthy""",

        "tips": """Soak chickpeas overnight
Mash few chickpeas for thick gravy
Garnish with coriander"""
    },

    {
        "title": "Crispy Masala Dosa",
        "recipe_name": "Masala Dosa",
        "category": "Indian",
        "excerpt": "Golden crispy dosa stuffed with spiced potato filling.",
        "content": "Masala dosa is a South Indian delicacy served with chutney and sambar.",
        "image_url": "images/indian/indian4.jpeg",
        "video_url": "https://www.youtube.com/embed/J75VQSxOtdo",

        "ingredients": """Dosa batter
Potatoes
Onion
Mustard seeds
Curry leaves
Turmeric
Oil
Salt""",

        "steps": """Prepare potato masala.
Heat tawa and spread batter.
Cook till crispy.
Add filling and fold dosa.
Serve hot.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 30 mins 🔥 Calories: ~350 kcal",

        "nutrition": """✅Fermented food
✅Easy to digest
✅Low fat
✅Gut friendly""",

        "tips": """Use fermented batter
Spread dosa thin
Serve immediately"""
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
        print("✅ Indian category blogs seeded successfully")

if __name__ == "__main__":
    run()