from flask import Blueprint
from app.file_controller import upload_file

routes = Blueprint("routes", __name__)

# رفع الملفات
routes.route("/upload", methods=["POST"])(upload_file)
