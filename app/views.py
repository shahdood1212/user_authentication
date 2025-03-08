from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from app import db
from app.models import User, File

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # إنشاء المجلد إذا لم يكن موجودًا
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'docx'}  # أنواع الملفات المسموح بها

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@jwt_required()
def upload_file():
    """ API لتحميل الملفات من قبل الطبيب أو المريض """

    # استخراج بيانات المستخدم من الـ JWT
    current_user = get_jwt_identity()
    uploader_id = current_user["user_id"]
    uploader_role = current_user["role"]

    # استخراج البيانات من الطلب
    user_id = request.form.get("user_id")
    phone_number = request.form.get("phone_number")
    country_code = request.form.get("country_code")
    result_date = request.form.get("resultDate")
    selected_lab_test = request.form.get("selectedLabTest")
    result_type = request.form.get("resultType")

    # التحقق من المدخلات الأساسية
    if not user_id or not result_date or not selected_lab_test or not result_type:
        return jsonify({"message": "Missing required fields"}), 400

    # البحث عن المستخدم المستهدف
    patient = User.query.filter_by(user_id=user_id, role="patient").first()
    if not patient:
        return jsonify({"message": "Patient not found"}), 404

    # التحقق من الصلاحيات: يجب أن يكون المستخدم طبيبًا أو مريضًا يريد تحميل ملف لنفسه
    if uploader_role == "patient" and uploader_id != int(user_id):
        return jsonify({"message": "Patients can only upload files for themselves"}), 403
    if uploader_role == "doctor" and uploader_id == int(user_id):
        return jsonify({"message": "Doctors cannot upload files for themselves"}), 403

    # التحقق من وجود ملف في الطلب
    if 'files' not in request.files:
        return jsonify({"message": "No file provided"}), 400

    file = request.files['files']
    
    # التأكد من صحة نوع الملف
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({"message": "Invalid file type"}), 400

    # حفظ الملف في السيرفر
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    # حفظ البيانات في قاعدة البيانات
    new_file = File(
        patient_id=user_id,
        uploader_id=uploader_id,
        file_name=filename,
        file_path=file_path,
        file_type=file.content_type,
        result_date=datetime.strptime(result_date, "%Y-%m-%d"),
        lab_test_type=selected_lab_test,
        result_type=result_type,
        status="pending"
    )
    
    db.session.add(new_file)
    db.session.commit()

    return jsonify({"message": "File uploaded successfully", "file_id": new_file.file_id}), 201


# @jwt_required()
# def get_profile(user_id):
#     current_user = get_jwt_identity()
#     # print(" Current User from Token:", current_user)  # ✅ لمعرفة القيم الفعلية

#     # التحقق من البيانات الفعلية القادمة من التوكن
#     if "user_id" not in current_user or "role" not in current_user:
#         return jsonify({"message": "Invalid token structure"}), 400

#     # السماح للمستخدم برؤية ملفه الشخصي أو السماح للمسؤول بالوصول إلى أي ملف شخصي
#     if current_user["user_id"] != user_id and current_user["role"] != "admin":
#         # print(" Access Denied for User ID:", current_user["user_id"])
#         return jsonify({"message": "Access forbidden"}), 403

#     # جلب المستخدم أو إرجاع 404 تلقائيًا
#     user = User.query.get_or_404(user_id, description="User not found")

#     return jsonify({
#         "status": "success",
#         "user": {
#             "user_id": user.user_id,
#             "email": user.email,
#             "role": user.role,
#             "first_name": user.first_name,
#             "last_name": user.last_name
#         }
#     }), 200
