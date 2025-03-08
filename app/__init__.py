from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # تهيئة الامتدادات
    migrate = Migrate()
    bcrypt = Bcrypt(app)
    jwt = JWTManager()

    # ربط الامتدادات مع التطبيق
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # استيراد وتسجيل الـ Blueprints
    from app.routes.auth import auth_bp
    from app.routes.users import users_bp  

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(users_bp, url_prefix="/api")

    from app.routes.routes import routes
    app.register_blueprint(routes)
    return app
