from flask import request
from db import db
from pydantic import ValidationError
from flask_restful import Resource
from app.models.product_model import ProductModel
from app.schemas.product_schema import CreateProductSchema

class ProductResource(Resource):
    def get(self):
        try:
            products = ProductModel.query.all()

            response_data = []
            for product in products:
                pass

            return response_data, 200
        except Exception as e:
            return {
                'message': 'Unexpected error',
            }, 500
        
    def post(self):
        try:
            validated_data = CreateProductSchema(
                name=request.form.get('name'),
                description=request.form.get('description'),
                brand=request.form.get('brand'),
                size=request.form.get('size'),
                price=request.form.get('price'),
                stock=request.form.get('stock'),
                category_id=request.form.get('category_id')
            )
            print(validated_data)
            # Validar la imagen
            return 'Ok', 200
        except Exception as e:
            print(e)
            return {
                'message': 'Unexpected error',
            }, 500