from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
from app.config.database import db
from datetime import datetime

bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = "users"
    
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False, default="patient", 
                     check_constraint="role IN ('patient', 'doctor', 'admin')")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    patient = db.relationship("Patient", back_populates="user", uselist=False)
    doctor = db.relationship("Doctor", back_populates="user", uselist=False)
    files = db.relationship("File", back_populates="uploader", lazy="dynamic")
    chat_sessions = db.relationship("ChatSession", back_populates="user", lazy="dynamic")
    user_sessions = db.relationship("UserSession", back_populates="user", lazy="dynamic")
    audit_logs = db.relationship("AuditLog", back_populates="user", lazy="dynamic")
   
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
    def __init__(self, username, email, role="patient", first_name="", last_name="", phone_number="", password=None):
        self.username = username
        self.email = email
        self.role = role
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

        if password:  
            self.set_password(password)
        else:
            self.password_hash = ""

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
