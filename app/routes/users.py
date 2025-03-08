from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User  

users_bp = Blueprint('users', __name__)

@users_bp.route('/profile/<int:user_id>', methods=['GET'])
@jwt_required()
def get_profile(user_id):
    current_user = get_jwt_identity()
    print("🔍 Current User from Token:", current_user)  # ✅ لمعرفة القيم الفعلية

    # التحقق من البيانات الفعلية القادمة من التوكن
    if "user_id" not in current_user or "role" not in current_user:
        return jsonify({"message": "Invalid token structure"}), 400

    # السماح للمستخدم برؤية ملفه الشخصي أو السماح للمسؤول بالوصول إلى أي ملف شخصي
    if current_user["user_id"] != user_id and current_user["role"] != "admin":
        print("🚫 Access Denied for User ID:", current_user["user_id"])
        return jsonify({"message": "Access forbidden"}), 403

    # جلب المستخدم أو إرجاع 404 تلقائيًا
    user = User.query.get_or_404(user_id, description="User not found")

    return jsonify({
        "status": "success",
        "user": {
            "user_id": user.user_id,
            "email": user.email,
            "role": user.role,
            "first_name": user.first_name,
            "last_name": user.last_name
        }
    }), 200
