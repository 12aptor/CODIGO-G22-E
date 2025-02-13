from flask_restful import Api
from app import app
from app.resources.role_resource import RoleResource
from app.resources.auth_resource import RegisterResource, LoginResource

api = Api(app, prefix='/api')

api.add_resource(RoleResource, '/roles')
api.add_resource(RegisterResource, '/auth/register')
api.add_resource(LoginResource, '/auth/login')