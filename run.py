from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
