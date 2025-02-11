# from werkzeug.security import generate_password_hash, check_password_hash
# from app.config.database import db

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128), nullable=False)  # ✅ لاحظ الاسم

#     role = db.Column(db.String(20), nullable=False, default="patient")
#     first_name = db.Column(db.String(50))
#     last_name = db.Column(db.String(50))
#     phone_number = db.Column(db.String(20))

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)  # ✅ تخزين كلمة المرور المشفرة

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)  # ✅ تحقق من كلمة المرور
