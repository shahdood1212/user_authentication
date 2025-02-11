import os

class Config:
    USE_POSTGRES = os.getenv('USE_POSTGRES', 'False').lower() == 'true'

    if USE_POSTGRES:
        POSTGRES_USER = os.getenv('POSTGRES_USER', 'shahd')
        POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'shahd')
        POSTGRES_DB = os.getenv('POSTGRES_DB', 'flask')
        POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
        POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')

        SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret')
    JWT_EXPIRATION_DELTA = 24  
    DEBUG = True

    # User Roles
    ROLES = ['patient', 'doctor']
