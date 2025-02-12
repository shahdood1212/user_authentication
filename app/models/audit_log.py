from app.config.database import db
from datetime import datetime

class AuditLog(db.Model):
    __tablename__ = "audit_logs"

    log_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    action_type = db.Column(db.String(50), nullable=False)
    action_details = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="audit_logs")
