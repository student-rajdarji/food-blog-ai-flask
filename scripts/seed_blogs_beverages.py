import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from models.blog import Blog
from slugify import slugify

blogs = [

    {
        "title": "Classic Refreshing Lemonade",
        "recipe_name": "Homemade Lemonade",
        "category": "Beverages",
        "excerpt": "Cool and zesty homemade lemonade to beat the heat.",
        "content": "A simple and refreshing lemonade made with fresh lemons, sugar, and a touch of mint.",
        "image_url": "images/beverages/beverages1.jpeg",
        "video_url": "https://www.youtube.com/embed/8ygXBT4P0fg",




        "ingredients": """Fresh lemon juice
Cold water
Sugar
Mint leaves
Ice cubes""",

        "steps": """Mix fresh lemon juice and sugar until dissolved.
Add cold water and stir.
Add mint leaves and ice cubes.
Serve chilled.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 10 mins 🔥 Calories: ~80 kcal",

        "nutrition": """✅ Hydrating
✅ Rich in vitamin C
✅ Refreshing
✅ Low calorie""",

        "tips": """Adjust sugar to taste
Add a pinch of salt
Use chilled lemons"""
    },

    {
        "title": "Creamy Mango Smoothie",
        "recipe_name": "Mango Smoothie",
        "category": "Beverages",
        "excerpt": "Thick and creamy smoothie bursting with mango flavor.",
        "content": "A tropical mango smoothie made with fresh fruit and yogurt for a creamy delight.",
        "image_url": "images/beverages/beverages2.jpeg",
        "video_url": "https://www.youtube.com/embed/BmZRf4kUTGg",

        "ingredients": """Ripe mango chunks
Yogurt
Milk
Honey
Ice cubes""",

        "steps": """Blend mango, yogurt, and milk until smooth.
Add honey and ice cubes.
Blend again.
Serve chilled.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 8 mins 🔥 Calories: ~200 kcal",

        "nutrition": """✅ Vitamin A rich
✅ High energy
✅ Calcium source
✅ Refreshing drink""",

        "tips": """Use chilled milk
Add banana for texture
Use honey for sweetness"""
    },

    {
        "title": "Traditional Masala Chai",
        "recipe_name": "Indian Masala Chai",
        "category": "Beverages",
        "excerpt": "Warm, spiced Indian tea for cozy mornings.",
        "content": "This classic masala chai combines tea leaves with aromatic spices for rich flavor.",
        "image_url": "images/beverages/beverages3.jpeg",
        "video_url": "https://www.youtube.com/embed/MKFIIzTJw1Y",

        "ingredients": """Water
Milk
Tea leaves
Sugar
Cardamom
Ginger""",

        "steps": """Boil water, ginger, and spices.
Add tea leaves and simmer.
Add milk and sugar.
Strain and serve hot.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 10 mins 🔥 Calories: ~120 kcal",

        "nutrition": """✅ Antioxidants
✅ Comfort drink
✅ Improves digestion""",

        "tips": """Use fresh spices
Do not over boil
Serve hot"""
    },

    {
        "title": "Iced Coffee Delight",
        "recipe_name": "Cold Iced Coffee",
        "category": "Beverages",
        "excerpt": "Chilled iced coffee with a creamy finish.",
        "content": "A delicious iced coffee that’s perfect for summer or anytime caffeine fix.",
        "image_url": "images/beverages/beverages4.jpeg",
        "video_url": "https://www.youtube.com/embed/PbKmZwniSF4",

        "ingredients": """Coffee
Milk
Ice cubes
Sugar
Cream""",

        "steps": """Brew strong coffee.
Mix with milk and sugar.
Pour over ice cubes.
Top with cream and serve.""",

        "serving_info": "🍽 Serves 2 ⏱ Prep time: 5 mins 🔥 Calories: ~190 kcal",

        "nutrition": """✅ Quick energy
✅ Refreshing
✅ Contains calcium""",

        "tips": """Use cold brew
Add caramel syrup
Serve with whipped cream"""
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
        print("✅ Beverages blogs seeded successfully")

if __name__ == "__main__":
    run()