from app import db
from datetime import datetime
from sqlalchemy import CheckConstraint

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), unique=True)
    country_code = db.Column(db.String(5))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(10))
    specialization = db.Column(db.String(100))
    license_number = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    from sqlalchemy import CheckConstraint

    __table_args__ = (    
        db.CheckConstraint(
            "(role = 'patient' AND phone_number IS NOT NULL AND country_code IS NOT NULL AND date_of_birth IS NOT NULL AND gender IS NOT NULL AND specialization IS NULL AND license_number IS NULL) OR"
            "(role = 'doctor' AND specialization IS NOT NULL AND license_number IS NOT NULL AND phone_number IS NULL AND country_code IS NULL AND date_of_birth IS NULL AND gender IS NULL) OR"
            "(role = 'admin' AND specialization IS NULL AND license_number IS NULL AND phone_number IS NULL AND country_code IS NULL AND date_of_birth IS NULL AND gender IS NULL)",
            name="patient_doctor_admin_check"
        ),
    )

class File(db.Model):
    __tablename__ = "files"

    file_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    uploader_id = db.Column(db.Integer, db.ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_type = db.Column(db.String(50))
    result_date = db.Column(db.Date)
    lab_test_type = db.Column(db.String(100))
    result_type = db.Column(db.String(50))
    status = db.Column(db.String(20), default="pending", server_default="pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        db.CheckConstraint("status IN ('pending', 'approved', 'rejected')", name="file_status_check"),
    )


# Chat Sessions Model
class ChatSession(db.Model):
    __tablename__ = "chat_sessions"
    
    session_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    session_number = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
# Chat Messages Model
class ChatMessage(db.Model):
    __tablename__ = "chat_messages"
    
    message_id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey("chat_sessions.session_id", ondelete="CASCADE"), nullable=False)
    file_id = db.Column(db.Integer, db.ForeignKey("files.file_id", ondelete="SET NULL"))
    message_text = db.Column(db.Text)
    response_text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
# User Sessions Model (JWT Token Management)
class UserSession(db.Model):
    __tablename__ = "user_sessions"
    
    session_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    token = db.Column(db.String(500), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
# Audit Logs Model
class AuditLog(db.Model):
    __tablename__ = "audit_logs"
    
    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    action_type = db.Column(db.String(50), nullable=False)
    action_details = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)