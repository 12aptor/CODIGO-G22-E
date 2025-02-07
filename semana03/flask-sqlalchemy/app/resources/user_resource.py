from flask_restful import Resource
from app.models.user_model import UserModel
from flask import request
from app.schemas.user_schema import UserCreateSchema, UserResponseSchema
from pydantic import ValidationError
from db import db

class UserResource(Resource):
    def get(self):
        try:
            users = UserModel.query.all()

            response_data = []
            for user in users:
                response_data.append(
                    UserResponseSchema(
                        id=user.id,
                        name=user.name,
                        email=user.email,
                        created_at=str(user.created_at)
                    ).model_dump()
                )
            return response_data, 200
        except Exception as e:
            return {
                'message': str(e)
            }, 500

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
            db.session.rollback()
            return {
                'message': str(e)
            }, 500
        
class UserManageResource(Resource):
    def get(self, user_id):
        try:
            user = UserModel.query.get(user_id)

            if not user:
                raise Exception('User not found')
            
            response_data = UserResponseSchema(
                id=user.id,
                name=user.name,
                email=user.email,
                created_at=str(user.created_at)
            )
            return response_data.model_dump(), 200
        except Exception as e:
            return {
                'message': str(e)
            }, 500
        
    def put(self, user_id):
        try:
            data = request.get_json()
            validated_data = UserCreateSchema(**data)

            user = UserModel.query.get(user_id)

            if not user:
                raise Exception('User not found')
            
            user.name = validated_data.name
            user.email = validated_data.email

            db.session.commit()

            response_data = UserResponseSchema(
                id=user.id,
                name=user.name,
                email=user.email,
                created_at=str(user.created_at)
            )
            return response_data.model_dump(), 200
        except ValidationError as e:
            return {
                'message': e.errors()
            }, 400
        except Exception as e:
            db.session.rollback()
            return {
                'message': str(e)
            }, 500
        
    def delete(self, user_id):
        try:
            user = UserModel.query.get(user_id)

            if not user:
                raise Exception('User not found')
            
            db.session.delete(user)
            db.session.commit()

            return {
                'message': 'User deleted successfully'
            }, 200
        except Exception as e:
            db.session.rollback()
            return {
                'message': str(e)
            }, 500