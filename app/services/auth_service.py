from app.config.database import db
from app.models.user import User
from werkzeug.security import check_password_hash

class AuthService:
    @staticmethod
    def create_user(data):
        if not data.get('username') or not data.get('email') or not data.get('password'):
            raise ValueError("Missing required fields")

        user = User(
            username=data['username'],
            email=data['email'],
            password=data['password'], 
            role=data.get('role', 'patient'),
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', ''),
            phone_number=data.get('phone_number', '')
        )

        db.session.add(user)
        db.session.commit()
        return user

    def authenticate_user(db, username, password):
        user = db.query(User).filter_by(username=username).first()  
        if user and user.check_password(password):  
            token = "mocked_token"  
            return user, token
        return None, None
class AuthService:
    @staticmethod
    def create_user(data):
        if not data.get('username') or not data.get('email') or not data.get('password'):
            raise ValueError("Missing required fields")

        user = User(
            username=data['username'],
            email=data['email'],
            role=data.get('role', 'patient'),
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', ''),
            phone_number=data.get('phone_number', '')
        )
        user.set_password(data['password'])  

        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def authenticate_user(db, username, password):
        user = db.query(User).filter_by(username=username).first()
        if user and user.check_password(password):  
            token = "mocked_token"  
            return user, token
        return None, None
