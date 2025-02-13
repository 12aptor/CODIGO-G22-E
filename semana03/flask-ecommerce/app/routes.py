from flask_restful import Api
from app import app
from app.resources.role_resource import RoleResource

api = Api(app, prefix='/api')

api.add_resource(RoleResource, '/roles')