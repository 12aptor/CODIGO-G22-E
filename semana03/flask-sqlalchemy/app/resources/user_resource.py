from flask_restful import Resource
from app.models.user_model import UserModel
from flask import request, jsonify
from app.schemas.user_schema import UserCreateSchema, UserResponseSchema
from pydantic import ValidationError
from db import db

class UserResource(Resource):
    def get(self):
        users = UserModel.query.all()
        print(users)
        return 'Ok'

    def post(self):
        try:
            data = request.get_json()
            validated_data = UserCreateSchema(**data)
            user = UserModel(
                name=validated_data.name,
                email=validated_data.email
            )
            db.session.add(user)
            db.session.commit()

            response_data = UserResponseSchema(
                id=user.id,
                name=user.name,
                email=user.email,
                created_at=str(user.created_at)
            )
            return response_data.model_dump(), 201
        except ValidationError as e:
            return {
                'message': e.errors()
            }, 400
        except Exception as e:
            return {
                'message': str(e)
            }, 500