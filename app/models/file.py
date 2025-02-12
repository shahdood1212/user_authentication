from app.config.database import db
from datetime import datetime

class File(db.Model):
    __tablename__ = "files"

    file_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.patient_id"), nullable=False)
    uploader_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_type = db.Column(db.String(50))
    result_date = db.Column(db.Date)
    lab_test_type = db.Column(db.String(100))
    result_type = db.Column(db.String(50))
    status = db.Column(db.String(20), nullable=False, default="pending", 
                       check_constraint="status IN ('pending', 'approved', 'rejected')")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    patient = db.relationship("Patient", back_populates="files")
    uploader = db.relationship("User", back_populates="files")
    chat_message = db.relationship("ChatMessage", back_populates="file", uselist=False)
