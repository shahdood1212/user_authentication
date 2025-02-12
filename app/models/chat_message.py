from app.config.database import db
from datetime import datetime

class ChatMessage(db.Model):
    __tablename__ = "chat_messages"

    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    session_id = db.Column(db.Integer, db.ForeignKey("chat_sessions.session_id"), nullable=False)
    file_id = db.Column(db.Integer, db.ForeignKey("files.file_id"), nullable=True)
    message_text = db.Column(db.Text)
    response_text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    
    session = db.relationship("ChatSession", back_populates="messages")
    file = db.relationship("File", back_populates="chat_message")
