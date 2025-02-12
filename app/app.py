from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import Config
from app.config.database import db
from app.models.user import bcrypt , User
from app.routes.auth_routes import auth_bp
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

def create_app():
    app = Flask(__name__)
    bcrypt = Bcrypt(app)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt = JWTManager(app)
    migrate = Migrate(app, db)
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
