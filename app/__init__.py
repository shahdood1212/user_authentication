from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

from app.config.config import Config
from app.config.database import db, init_db
from app.routes.auth_routes import auth_bp

bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    JWTManager(app)
    Migrate(app, db)

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    init_db(app)
    
    with app.app_context():
        db.create_all()  
    return app
