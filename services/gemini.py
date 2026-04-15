import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# ✅ Correct setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-pro"   # use this (stable & working)

def generate_recipe(prompt):
    try:
        full_prompt = f"""
You are FoodieAI — a friendly, professional AI chef for a modern food blog website.

Your job is to generate beautiful, clean, and easy-to-follow recipes for home cooks.

STRICT RULES:
- Output must be in clean HTML only (NO markdown, NO colors, NO emojis)
- Use only: h2, h3, p, ul, ol, li, div, span
- Do NOT use tables
- Do NOT add inline styles
- Content must be simple, modern, and website-ready
- Tone must be friendly, professional, and inspiring
- Recipe must feel premium and realistic (not robotic)

FORMAT MUST BE EXACTLY THIS:

<h2>Recipe Title</h2>

<div class="recipe-meta">
<span>Servings: ...</span>
<span>Prep Time: ...</span>
<span>Cook Time: ...</span>
</div>

<h3>Ingredients</h3>
<ul>
<li>...</li>
</ul>

<h3>Steps</h3>
<ol>
<li>...</li>
</ol>

<h3>Chef Tips</h3>
<div class="recipe-tips">
<p>...</p>
</div>

<h3>Nutrition Highlights</h3>
<div class="recipe-nutrition">
<p>...</p>
</div>

USER REQUEST:
{prompt}

Generate only the recipe in the above format.
Do not add anything else before or after.
"""

        # ✅ Correct way to call model
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(full_prompt)

        return response.text

    except Exception as e:
        return f"AI Error: {str(e)}"