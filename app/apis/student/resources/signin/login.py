import json
import requests
import traceback
from flask import make_response, jsonify, current_app, request
from flask_restful import Resource, reqparse
from flask_sieve import Validator



class StudentLogin(Resource):
    @classmethod
    def get(cls):
        return {'hello': 'world'}


    @classmethod
    def post(cls):
        try:
            response = {
                "status": "success",
                "status_code": 200,
                "message": "SUCCESS",
                "data": "shamir",
            }
            return make_response(jsonify(response), 200)
        except Exception as err:
            current_app.logger.error(traceback.format_exc())
            response = {
                "status": "error",
                "status_code": 500,
                "message": "System Error",
                "data": {},
            }
            return make_response(jsonify(response), 500)