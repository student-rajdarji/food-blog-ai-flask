from flask import Blueprint, request, render_template
from sqlalchemy import or_
from models.blog import Blog

search_bp = Blueprint('search', __name__)

@search_bp.route('/search')
def search():
    query = request.args.get('query', '').strip()

    blogs = []

    if query:
        blogs = Blog.query.filter(
            or_(
                Blog.title.ilike(f"%{query}%"),
                Blog.content.ilike(f"%{query}%"),
                Blog.category.ilike(f"%{query}%")
            )
        ).order_by(Blog.created_at.desc()).all()

    return render_template(
        'search_results.html',
        blogs=blogs,
        query=query
    )