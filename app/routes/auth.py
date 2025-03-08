from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from utils import hash_password, check_password, generate_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    if "password" not in data:
        return jsonify({"error": "Password is required"}), 400
    
    hashed_password = hash_password(data["password"])  # تأكد من تشفير كلمة المرور
        
    new_user = User(
        username=data["username"],
        password_hash=hashed_password,
        email=data["email"],
        role=data["role"],
        first_name=data["first_name"],
        last_name=data["last_name"],
        phone_number=data.get("phone_number"),
        country_code=data.get("country_code"),
        date_of_birth=data.get("date_of_birth"),
        gender=data.get("gender"),
        specialization=data.get("specialization"),
        license_number=data.get("license_number"),
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User created successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    print("Received login request:", data)

    user = User.query.filter_by(email=data["email"]).first()
    if not user:
        print("User not found!")
        return jsonify({"message": "Invalid email or password"}), 401

    if not check_password(user.password_hash, data["password"]):
        print("Password mismatch!")
        return jsonify({"message": "Invalid email or password"}), 401

    access_token = generate_token(user)
    return jsonify({'access_token': access_token}), 200