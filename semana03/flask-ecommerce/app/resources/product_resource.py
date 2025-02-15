from flask import request
from db import db
from pydantic import ValidationError
from flask_restful import Resource
from app.models.product_model import ProductModel
from app.schemas.product_schema import (
    CreateProductSchema,
    ProductSchema
)
import app.utils.cloudinary_config
import cloudinary.uploader
import uuid

class ProductResource(Resource):
    def get(self):
        try:
            products = ProductModel.query.all()

            response_data = []
            for product in products:
                response_data.append(
                    ProductSchema(
                        id=product.id,
                        code=product.code,
                        name=product.name,
                        image=cloudinary.utils.cloudinary_url(product.image)[0],
                        description=product.description,
                        brand=product.brand,
                        size=product.size,
                        price=product.price,
                        stock=product.stock,
                        status=product.status,
                        created_at=str(product.created_at),
                        updated_at=str(product.updated_at),
                        category_id=product.category_id
                    ).model_dump()
                )

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

            image = request.files.get('image')

            if not image.content_type.startswith('image/'):
                raise ValidationError('Invalida image format')
            
            file_size = image.read()
            image.seek(0)
            kb_size = len(file_size) / 1024
            mb_size = kb_size / 1024

            if mb_size > 2:
                raise ValidationError('Image size is too big')
            
            filename = image.filename.split('.')[0]
            public_id = f'{uuid.uuid4()}-{filename}'

            cloudinary.uploader.upload(
                file=image.stream,
                public_id=public_id
            )

            last_product = ProductModel.query.order_by(
                ProductModel.id.desc()
            ).first()

            product_code = 'P-0001'
            if last_product:
                last_code = last_product.code
                last_number = int(last_code.split('-')[1])
                new_number = last_number + 1
                product_code = 'P-' + str(new_number).zfill(4)

            product = ProductModel(
                name=validated_data.name,
                code=product_code,
                description=validated_data.description,
                image=public_id,
                brand=validated_data.brand,
                size=validated_data.size,
                price=validated_data.price,
                stock=validated_data.stock,
                category_id=validated_data.category_id
            )
            db.session.add(product)
            db.session.commit()

            response_data = ProductSchema(
                id=product.id,
                code=product.code,
                name=product.name,
                image=cloudinary.utils.cloudinary_url(product.image)[0],
                description=product.description,
                brand=product.brand,
                size=product.size,
                price=product.price,
                stock=product.stock,
                status=product.status,
                created_at=str(product.created_at),
                updated_at=str(product.updated_at),
                category_id=product.category_id
            )
            return response_data.model_dump(), 200
        except ValidationError as e:
            return {
                'message', e.errors()
            }, 400
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Unexpected error',
            }, 500