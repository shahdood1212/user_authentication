import jwt
import datetime
from app.config.settings import Config

class TokenManager:
    """Manages JWT token generation and validation"""
    
    @staticmethod
    def generate_token(user):
        """
        Generate JWT token for authenticated user
        
        Args:
            user (User): User object to generate token for
        
        Returns:
            str: JWT token
        """
        payload = {
            'user_id': user.id,
            'username': user.username,
            'role': user.role,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=Config.JWT_EXPIRATION_DELTA)
        }
        return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')

    @staticmethod
    def decode_token(token):
        """
        Decode and validate JWT token
        
        Args:
            token (str): JWT token to decode
        
        Returns:
            dict: Decoded token payload or None if invalid
        """
        try:
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None