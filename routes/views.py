from flask import Blueprint, render_template
from flask_login import login_required, current_user

blog_bp = Blueprint('blog', __name__)


