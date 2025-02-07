from flask_restful import Api
from app.resources.user_resource import UserResource, UserManageResource
from app import app

api = Api(app, prefix='/api')

api.add_resource(UserResource, '/users')
api.add_resource(UserManageResource, '/users/<int:user_id>')