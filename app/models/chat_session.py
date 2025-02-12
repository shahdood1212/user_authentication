from app.config.database import db
from datetime import datetime

class ChatSession(db.Model):
    __tablename__ = "chat_sessions"

    session_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    session_number = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="chat_sessions")
    messages = db.relationship("ChatMessage", back_populates="session", lazy="dynamic")
