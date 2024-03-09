from flask import Blueprint
from flask_restful import Api
from .routes import initialize_routes

studentApp = Blueprint("student", __name__, template_folder="templates", url_prefix="/student")
student_app = Api(studentApp)
initialize_routes(student_app)