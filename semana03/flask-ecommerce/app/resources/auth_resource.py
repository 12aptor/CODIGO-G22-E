from app.models.user_model import UserModel
from flask_restful import Resource
from flask import request
from app.schemas.auth_schema import RegisterSchema, UserSchema
from pydantic import ValidationError
from app.utils.passwords import hash_password
from db import db

class RegisterResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            validated_data = RegisterSchema(**data)

            existing_user = UserModel.query.filter_by(email=validated_data.email).first()

            if existing_user:
                return {
                    'message': 'User already exists'
                }, 400

            user = UserModel(
                name=validated_data.name,
                last_name=validated_data.last_name,
                email=validated_data.email,
                password=hash_password(validated_data.password),
                role_id=validated_data.role_id
            )
            db.session.add(user)
            db.session.commit()

            response_data = UserSchema(
                id=user.id,
                name=user.name,
                last_name=user.last_name,
                email=user.email,
                status=user.status,
                created_at=str(user.created_at),
                updated_at=str(user.updated_at),
                role_id=user.role_id
            )

            return response_data.model_dump(), 200
        except ValidationError as e:
            return {
                'message': e.errors()
            }, 400
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Unexpected error',
            }, 500

class LoginResource(Resource):
    def post(self):
        try:
            pass
        except Exception as e:
            pass