import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from flask import session
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app.config.database import db
import jwt
import datetime

class AuthService:
    @staticmethod
    def create_user(data):
        try:
            new_user = User(
                username=data["username"],
                email=data["email"],
                password=data["password"],  
                role=data.get("role", "patient"),
                first_name=data.get("first_name", ""),
                last_name=data.get("last_name", ""),
                phone_number=data["phone_number"]
            )

            db.session.add(new_user)
            db.session.commit()
            return new_user, "User created successfully"

        except IntegrityError:
            db.session.rollback()
            return None, "Email or phone number is already in use"

        except Exception as e:
            return None, f"Unexpected error: {str(e)}"

    @staticmethod
    def authenticate_user(username, password):
        session = db.session
        user = session.query(User).filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            token = jwt.encode(
                {
                    "user_id": user.id,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
                },
                "SECRET_KEY", 
                algorithm="HS256"
            )
            return user, token

        return None, None
