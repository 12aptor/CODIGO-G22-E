from flask_restful import Resource
from app.models.user_model import UserModel

class UserResource(Resource):
    def get(self):
        users = UserModel.query.all()
        print(users)
        return 'Ok'

    def post(self):
        pass