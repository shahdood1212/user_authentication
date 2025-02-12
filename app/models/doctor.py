from app.config.database import db

class Doctor(db.Model):
    __tablename__ = "doctors"

    doctor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    specialization = db.Column(db.String(100))
    license_number = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    country_code = db.Column(db.String(5))

    user = db.relationship("User", back_populates="doctor")
