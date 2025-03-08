# from app import bcrypt
from flask_jwt_extended import create_access_token
import datetime
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password(hashed_password, plain_password):
    return bcrypt.check_password_hash(hashed_password, plain_password)

# def generate_token(user):
#     return create_access_token(
#         identity={'user_id': user.user_id, 'role': user.role},
#         expires_delta=datetime.timedelta(days=1)
#     )


def generate_token(user):
    return create_access_token(
        identity={"user_id": user.user_id, "role": user.role},
        expires_delta=datetime.timedelta(days=1)
    )
