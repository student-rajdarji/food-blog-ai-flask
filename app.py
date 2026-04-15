from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
from extensions import db, login_manager, migrate
from models.blog import Blog


def create_app():
    app = Flask(
        __name__,
        static_folder="static",
        static_url_path="/static"
    )
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        from models.user import User
        return User.query.get(int(user_id))

    import models

    from routes.auth_routes import auth_bp
    from routes.blog_routes import blog_bp
    from routes.save_routes import save_bp
    from routes.ai_routes import ai_bp
    from routes.recipe_save_routes import recipe_save_bp
    from routes.pdf_routes import pdf_bp
    from routes.ai_save_routes import ai_save_bp
    from routes.saved_routes import saved_bp
    from routes.category_routes import category_bp
    from routes.admin_routes import admin_bp
    from routes.recipe_routes import recipe_bp
    from routes.comment_routes import comment_bp
    from routes.seach_routes import search_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(save_bp)
    app.register_blueprint(ai_bp)
    app.register_blueprint(recipe_save_bp)
    app.register_blueprint(pdf_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(ai_save_bp)
    app.register_blueprint(saved_bp)
    app.register_blueprint(recipe_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(comment_bp)
    app.register_blueprint(search_bp)

    @app.route("/")
    def home():
        blogs = (
            Blog.query
            .filter_by(is_featured=True)
            .order_by(Blog.id.asc())
            .all()
        )
        return render_template("home.html", blogs=blogs)

    return app