from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
from app.config.database import db

bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, username, email, password, role, first_name, last_name, phone_number):
        self.username = username
        self.email = email
        self.set_password(password)  
        self.role = role
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number
        }
