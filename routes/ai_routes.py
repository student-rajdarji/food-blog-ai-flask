from flask import Blueprint, render_template, request, session
from flask_login import current_user
from services.gemini import generate_recipe
from extensions import db
from models.saved_ai_recipe import SavedAIRecipe

ai_bp = Blueprint("ai", __name__)

@ai_bp.route("/ai-generator", methods=["GET", "POST"])
def ai_generator():

    recipe = None
    recipe_title = None

    # ===============================
    # 🎯 CATEGORY → AUTO PROMPT
    # ===============================
    category = request.args.get("category")

    category_prompts = {
        "healthy": "Generate a healthy and nutritious recipe",
        "spicy": "Generate a spicy and flavorful recipe",
        "diet": "Generate a low calorie diet-friendly recipe",
        "breakfast": "Generate a quick and healthy breakfast recipe",
        "vegan": "Generate a 100% vegan recipe",
        "fast_food": "Generate a fast food style recipe",
        "indian": "Generate an Indian recipe",
        "italian": "Generate an Italian recipe",
        "desserts": "Generate a dessert recipe",
        "beverages": "Generate a beverage recipe",
        "high_protein": "Generate a high protein recipe",
        "quick_easy": "Generate a quick and easy recipe"
    }

    auto_prompt = category_prompts.get(category)

    # ===============================
    # 🔐 LOGGED-IN USER → DB HISTORY
    # ===============================
    if current_user.is_authenticated:
        history = (
            SavedAIRecipe.query
            .filter_by(user_id=current_user.id)
            .order_by(SavedAIRecipe.created_at.desc())
            .all()
        )
    else:
        if "recipe_history" not in session:
            session["recipe_history"] = []
        history = session["recipe_history"]

    # ===============================
    # LOAD RECIPE FROM HISTORY
    # ===============================
    load_index = request.args.get("load")
    if load_index is not None:
        try:
            load_index = int(load_index)
            item = history[load_index]

            if current_user.is_authenticated:
                recipe = item.recipe
                recipe_title = item.title
            else:
                recipe = item["recipe"]
                recipe_title = item["title"]

            session["last_recipe"] = recipe
            session["last_recipe_title"] = recipe_title
        except Exception:
            pass

    # ===============================
    # GENERATE NEW RECIPE
    # ===============================
    if request.method == "POST":
        prompt = request.form.get("prompt")

        if prompt:
            recipe = generate_recipe(prompt)

            if "<h2>" in recipe:
                recipe_title = recipe.split("<h2>")[1].split("</h2>")[0]
            else:
                recipe_title = "AI Recipe"

            session["last_recipe"] = recipe
            session["last_recipe_title"] = recipe_title
            session.modified = True

            if current_user.is_authenticated:
                new_recipe = SavedAIRecipe(
                    user_id=current_user.id,
                    title=recipe_title,
                    recipe=recipe
                )
                db.session.add(new_recipe)
                db.session.commit()
                history.insert(0, new_recipe)
            else:
                session["recipe_history"].insert(0, {
                    "title": recipe_title,
                    "recipe": recipe
                })
                session.modified = True

    return render_template(
        "ai_generator.html",
        recipe=recipe,
        recipe_title=recipe_title,
        history=history,
        auto_prompt=auto_prompt
    )