from app import create_app
from extensions import db
from models.blog import Blog
from slugify import slugify
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

blogs = [
    {
        "title": "Healthy Breakfast Ideas for Busy Mornings",
        "recipe_name": "Fruit & Nut Oatmeal Bowl",
        "category": "Healthy",
        "excerpt": "Quick and nutritious breakfast ideas for busy mornings.",
        "content": "Detailed recipe here...",
        "image_url": "images/healthy/healthy1.jpeg",
        "video_url": "https://www.youtube.com/embed/LtnrmEd_msY"
    },
    {
        "title": "Low-Calorie Healthy Lunch Recipes",
        "recipe_name": "Grilled Veggie Quinoa Salad",
        "category": "Healthy",
        "excerpt": "Light and filling lunch recipes.",
        "content": "Detailed recipe here...",
        "image_url": "images/healthy/healthy2.jpeg",
        "video_url": "https://www.youtube.com/embed/uK4LibynqSk"
    },
    {
        "title": "Healthy Evening Snacks to Stay Full",
        "recipe_name": "Roasted Chickpea Chaat",
        "category": "Healthy",
        "excerpt": "Healthy evening snacks.",
        "content": "Detailed recipe here...",
        "image_url": "images/healthy/healthy3.jpeg",
        "video_url": "https://www.youtube.com/embed/EfxM7zEGs1k"
    },
    {
        "title": "Nutritious Healthy Dinner Meals",
        "recipe_name": "Veggie Brown Rice Bowl",
        "category": "Healthy",
        "excerpt": "Nutritious dinner ideas.",
        "content": "Detailed recipe here...",
        "image_url": "images/healthy/healthy4.jpeg",
        "video_url": "https://www.youtube.com/embed/m_4sCZDyAIw"
    }
]

def run():
    app = create_app()
    with app.app_context():
        # 🔥 DELETE OLD HEALTHY BLOGS
        Blog.query.filter_by(category="Healthy").delete()
        db.session.commit()

        for b in blogs:
            blog = Blog(
                title=b["title"],
                slug=slugify(b["title"]),
                excerpt=b["excerpt"],
                content=b["content"],
                image_url=b["image_url"],
                category=b["category"],
                recipe_name=b["recipe_name"],
                video_url=b["video_url"]
            )
            db.session.add(blog)

        db.session.commit()
        print("✅ Healthy blogs reseeded WITH videos")

if __name__ == "__main__":
    run()