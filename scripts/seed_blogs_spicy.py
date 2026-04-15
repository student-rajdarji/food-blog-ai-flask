import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from models.blog import Blog
from slugify import slugify

blogs = [
    {
        "title": "Spicy Garlic Chicken Stir-Fry",
        "recipe_name": "Garlic Chili Chicken",
        "category": "Spicy",
        "excerpt": "Juicy chicken tossed in fiery garlic chili sauce.",
        "content": "A bold and spicy chicken stir-fry packed with garlic and chili flavors.",
        "image_url": "images/spicy/spicy1.jpeg",
        "video_url": "https://www.youtube.com/embed/j1Jq8JjvSMc",

        "ingredients": """Boneless chicken (cubed)
Garlic (minced)
Dry red chilies
Soy sauce
Chili sauce
Vinegar
Spring onions
Oil, salt & pepper""",

        "steps": """Heat oil and sauté garlic with red chilies.
Add chicken and cook until golden.
Mix soy sauce, chili sauce, and vinegar.
Toss well and garnish with spring onions.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 15 mins 🔥 Calories: ~320 kcal",

        "nutrition": """✅ High protein
✅ Boosts metabolism
✅ Low carbs
✅ Energy rich""",

        "tips": """Add bell peppers for crunch
Use paneer for veg option
Increase chili oil for extra heat"""
    },

    {
        "title": "Fiery Paneer Tikka",
        "recipe_name": "Spicy Grilled Paneer",
        "category": "Spicy",
        "excerpt": "Smoky paneer cubes grilled with bold Indian spices.",
        "content": "A classic spicy paneer tikka perfect for starters or dinner.",
        "image_url": "images/spicy/spicy2.jpeg",
        "video_url": "https://www.youtube.com/embed/BwIJHI4KdIE",

        "ingredients": """Paneer cubes
Thick curd
Red chili powder
Garam masala
Ginger-garlic paste
Lemon juice
Capsicum & onion""",

        "steps": """Mix curd and spices to prepare marinade.
Coat paneer and vegetables.
Rest for 30 minutes.
Grill or pan roast until charred.""",

        "serving_info": "🍽 Serves 3 ⏱ Prep time: 30 mins 🔥 Calories: ~280 kcal",

        "nutrition": """✅ High calcium
✅ Protein rich
✅ Vegetarian friendly
✅ Filling snack""",

        "tips": """Add kasuri methi for aroma
Air-fryer works great
Serve with mint chutney"""
    },

    {
        "title": "Spicy Schezwan Noodles",
        "recipe_name": "Chili Garlic Noodles",
        "category": "Spicy",
        "excerpt": "Street-style noodles with fiery schezwan sauce.",
        "content": "A quick and spicy noodle recipe loaded with garlic and vegetables.",
        "image_url": "images/spicy/spicy3.jpeg",
        "video_url": "https://www.youtube.com/embed/HFUt5JOdHhI",

        "ingredients": """Boiled noodles
Schezwan sauce
Garlic (chopped)
Mixed vegetables
Soy sauce
Chili flakes
Spring onions""",

        "steps": """Heat oil and sauté garlic.
Add vegetables and stir fry on high heat.
Mix sauces and noodles.
Toss well and garnish.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 20 mins 🔥 Calories: ~350 kcal",

        "nutrition": """✅ Energy boosting
✅ Fiber rich
✅ Vegan friendly
✅ Street-style taste""",

        "tips": """Add tofu or chicken
Use whole wheat noodles
Top with chili oil"""
    },

    {
        "title": "Hot and Spicy Chicken Wings",
        "recipe_name": "Chili Glazed Wings",
        "category": "Spicy",
        "excerpt": "Crispy wings coated in sticky spicy chili glaze.",
        "content": "Perfect party-style chicken wings with bold spicy flavors.",
        "image_url": "images/spicy/spicy4.jpeg",
        "video_url": "https://www.youtube.com/embed/7UpgXyKA_-E",

        "ingredients": """Chicken wings
Red chili sauce
Honey
Garlic powder
Paprika
Butter
Salt""",

        "steps": """Bake or fry wings until crispy.
Prepare chili-honey glaze.
Toss wings in sauce.
Serve hot with dip.""",

        "serving_info": "🍽 Serves 4 ⏱ Prep time: 40 mins 🔥 Calories: ~420 kcal",

        "nutrition": """✅ High protein
✅ Energy dense
✅ Party favorite
✅ Satisfying snack""",

        "tips": """Use air fryer for healthier version
Add smoked paprika
Serve with ranch dip"""
    }
]

def run():
    app = create_app()
    with app.app_context():
        for b in blogs:
            slug = slugify(b["title"])
            blog = Blog.query.filter_by(slug=slug).first()

            if blog:
                # UPDATE existing blog
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
        print("✅ Spicy blogs seeded successfully")

if __name__ == "__main__":
    run()