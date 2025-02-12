from app.config.database import db

class Patient(db.Model):
    __tablename__ = "patients"

    patient_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    country_code = db.Column(db.String(5), nullable=False)
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(10))

    
    __table_args__ = (db.UniqueConstraint("phone_number", "country_code", name="unique_phone"),)

    user = db.relationship("User", back_populates="patient")
    files = db.relationship("File", back_populates="patient", lazy="dynamic")
