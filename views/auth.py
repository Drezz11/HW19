from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import genre_service, user_service
from service.auth import generate_token, approve_token

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get("username")
        password = req_json.get("password")

        if not username and password:
            return "что то не передано", 401

        user = user_service.get_by_username(username=username)
        if user:
            return generate_token(
                username=username,
                password=password,
                password_hash=user.password,
                is_refresh=False
            )


    def put(self):
        req_json = request.json

        if not req_json.get("refresh"):
            return "refresh_token не передан", 401

        return approve_token(
            token=req_json.get("refresh_token")
        ), 200


