from flask import Blueprint, request, jsonify
from app.config.database import db, get_db
from app.services.auth_service import AuthService
import traceback

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        user = AuthService.create_user(data)  
        return jsonify({"message": "User created successfully", "user_id": user.id}), 201

    except Exception as e:
        print("Signup Error:", str(e))
        traceback.print_exc()  
        return jsonify({"error": str(e)}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        db = get_db()   
        data = request.get_json()

        if not data or 'username' not in data or 'password' not in data:
            return jsonify({'error': 'Username and password are required'}), 400

        user, token = AuthService.authenticate_user(db, data['username'], data['password'])
        if user and token:
            return jsonify({'token': token, 'user': user.to_dict()}), 200

        return jsonify({'error': 'Invalid credentials'}), 401

    except Exception as e:
        print("Login Error:", str(e))
        traceback.print_exc() 
        return jsonify({'error': str(e)}), 500
