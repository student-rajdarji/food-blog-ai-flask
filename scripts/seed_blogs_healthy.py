import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from models.blog import Blog
from slugify import slugify

blogs = [
    {
        "title": "Healthy Breakfast Ideas for Busy Mornings",
        "recipe_name": "Fruit & Nut Oatmeal Bowl",
        "category": "Healthy",
        "excerpt": "Quick and nutritious breakfast ideas for busy mornings.",
        "content": "A nourishing oatmeal bowl packed with fruits and nuts to start your day right.",
        "image_url": "images/healthy/healthy1.jpeg",
        "video_url": "https://www.youtube.com/embed/LtnrmEd_msY",

        "ingredients": """Rolled oats
 Milk or water
 Banana slices
 Berries
 Almonds & walnuts
 Honey or maple syrup""",

        "steps": """ Cook oats with milk or water.
 Transfer to a bowl.
 Add fruits and nuts.
 Drizzle honey and serve warm.""",

        "serving_info": "🍽 Serves 1 ⏱ Prep time: 5 mins 🔥 Calories: ~280 kcal",

        "nutrition": """✅High fiber
✅Rich in antioxidants
✅ Energy boosting
✅ Heart healthy""",

        "tips": """ Use almond milk for vegan option
Add chia seeds for extra fiber
 Use peanut butter for more protein"""
    },

    {
        "title": "Low-Calorie Healthy Lunch Recipes",
        "recipe_name": "Grilled Veggie Quinoa Salad",
        "category": "Healthy",
        "excerpt": "Light and filling lunch recipes.",
        "content": "A refreshing quinoa salad loaded with grilled vegetables and light dressing.",
        "image_url": "images/healthy/healthy2.jpeg",
        "video_url": "https://www.youtube.com/embed/uK4LibynqSk",

        "ingredients": """ Cooked quinoa
 Bell peppers
 Zucchini
Olive oil
 Lemon juice
 Salt & pepper""",

        "steps": """ Grill vegetables lightly.
 Mix vegetables with cooked quinoa.
 Add olive oil and lemon juice.
 Toss well and serve.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 15 mins 🔥 Calories: ~350 kcal",

        "nutrition": """ ✅High protein
✅Low calorie
✅Gluten free
✅ Keeps you full longer""",

        "tips": """ Add feta cheese for taste
 Replace quinoa with millet
 Add chickpeas for more protein"""
    },

    {
        "title": "Healthy Evening Snacks to Stay Full",
        "recipe_name": "Roasted Chickpea Chaat",
        "category": "Healthy",
        "excerpt": "Healthy evening snacks.",
        "content": "Crunchy roasted chickpeas mixed with spices and lemon for a perfect snack.",
        "image_url": "images/healthy/healthy3.jpeg",
        "video_url": "https://www.youtube.com/embed/EfxM7zEGs1k",

        "ingredients": """Boiled chickpeas
Onion (finely chopped)
Tomato
 Lemon juice
 Chaat masala
 Salt & pepper""",

        "steps": """Roast chickpeas until crispy.
 Add onion and tomato.
 Sprinkle spices and lemon juice.
 Mix and serve fresh.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 10 mins 🔥 Calories: ~200 kcal",

        "nutrition": """ ✅High protein
✅High fiber
✅Low fat
✅ Boosts metabolism""",

        "tips": """ Use air fryer for less oil
 Add cucumber for crunch
Sprinkle roasted peanuts"""
    },

    {
        "title": "Nutritious Healthy Dinner Meals",
        "recipe_name": "Veggie Brown Rice Bowl",
        "category": "Healthy",
        "excerpt": "Nutritious dinner ideas.",
        "content": "A wholesome dinner bowl with brown rice and sautéed vegetables.",
        "image_url": "images/healthy/healthy4.jpeg",
        "video_url": "https://www.youtube.com/embed/m_4sCZDyAIw",

        "ingredients": """Cooked brown rice
Mixed vegetables
Olive oil
 Garlic
 Soy sauce
 Spring onions""",

        "steps": """ Sauté garlic in olive oil.
Add vegetables and stir fry.
Mix with cooked brown rice.
Garnish with spring onions.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 20 mins 🔥 Calories: ~420 kcal",

        "nutrition": """✅Rich in complex carbs
 ✅High fiber
 ✅Balanced nutrients
 ✅Good for digestion""",

        "tips": """ Add tofu for protein
 Use low sodium soy sauce
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
        print("✅ Healthy blogs updated successfully")

if __name__ == "__main__":
    run()