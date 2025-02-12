from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService
import traceback

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def register():
    try:
        data = request.get_json()
        user, message = AuthService.create_user(data)

        if not user:
            return jsonify({"error": message}), 400

        return jsonify({"message": message, "user_id": user.id}), 201

    except Exception as e:
        print("Signup Error:", str(e))
        traceback.print_exc()
        return jsonify({"error": "An unexpected error occurred"}), 500

@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()

        if not data or "username" not in data or "password" not in data:
            return jsonify({"error": "Username and password are required"}), 400

        user, token = AuthService.authenticate_user(data["username"], data["password"])

        if user and token:
            return jsonify({"token": token, "user": {"id": user.id, "username": user.username}}), 200

        return jsonify({"error": "Invalid login credentials"}), 401

    except Exception as e:
        print("Login Error:", str(e))
        traceback.print_exc()
        return jsonify({"error": "An unexpected error occurred"}), 500
