from flask_restful import Resource
from app.models.user_model import UserModel
from flask import request
from app.schemas.user_schema import UserCreateSchema
from pydantic import ValidationError

class UserResource(Resource):
    def get(self):
        users = UserModel.query.all()
        print(users)
        return 'Ok'

    def post(self):
        try:
            data = request.get_json()
            validated_data = UserCreateSchema(**data)
            print(validated_data.name)
            print(validated_data.email)
            return 'Ok'
        except ValidationError as e:
            print(e.errors())
        except Exception as e:
            print(e)