from flask import Blueprint, session, send_file, flash, redirect, url_for
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import io
import re
from html import unescape

pdf_bp = Blueprint("pdf", __name__)

def clean_html_to_text(html):
    """
    Converts HTML recipe into clean plain text for PDF
    """
    # Remove all HTML tags
    text = re.sub(r"<[^>]+>", "", html)

    # Unescape HTML entities
    text = unescape(text)

    # Normalize spacing
    text = re.sub(r"\n\s*\n", "\n\n", text)
    return text.strip()


@pdf_bp.route("/download-pdf", methods=["GET"])
def download_pdf():
    recipe_html = session.get("last_recipe")
    title = session.get("last_recipe_title", "AI Recipe")

    if not recipe_html:
        flash("No recipe to download", "danger")
        return redirect(url_for("ai.ai_generator"))

    # ✅ CLEAN HTML SAFELY
    recipe_text = clean_html_to_text(recipe_html)

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph(title, styles["Title"]))
    story.append(Spacer(1, 14))

    # Content
    for line in recipe_text.split("\n"):
        if line.strip():
            story.append(Paragraph(line, styles["Normal"]))
            story.append(Spacer(1, 8))

    doc.build(story)
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"{title}.pdf",
        mimetype="application/pdf",
    )