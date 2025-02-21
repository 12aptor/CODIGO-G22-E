from flask_restful import Resource
from app.models.sale_model import SaleModel
from flask import request
from app.schemas.sale_schema import (
    CreateSaleSchema,
    SaleSchema
)
from app.models.customer_model import CustomerModel
from app.models.sale_detail_model import SaleDetailModel
from app.models.product_model import ProductModel
from db import db

class SaleResource(Resource):
    def get(self):
        try:
            sales = SaleModel.query.all()

            response_data = []
            for sale in sales:
                response_data.append(
                    SaleSchema(
                        id=sale.id,
                        code=sale.code,
                        total=sale.total,
                        status=sale.status,
                        created_at=str(sale.created_at),
                        updated_at=str(sale.updated_at),
                        customer_id=sale.customer_id
                    ).model_dump()
                )

            return response_data, 200
        except Exception as e:
            return {
                'message': 'Unexpected error',
            }, 500

    def post(self):
        try:
            data = request.get_json()
            validated_data = CreateSaleSchema(**data)

            customer = CustomerModel.query.filter_by(
                document_number=validated_data.customer.document_number
            ).first()

            if not customer:
                customer = CustomerModel(
                    name=validated_data.customer.name,
                    last_name=validated_data.customer.last_name,
                    email=validated_data.customer.email,
                    address=validated_data.customer.address,
                    document_number=validated_data.customer.document_number
                )

                db.session.add(customer)
                db.session.flush()
            else:
                customer.name = validated_data.customer.name
                customer.last_name = validated_data.customer.last_name
                customer.email = validated_data.customer.email
                customer.address = validated_data.customer.address

            sale_details = []
            for detail in validated_data.details:
                product = ProductModel.query.get(detail.product_id)
                if not product:
                    raise Exception('Product not found')
                
                if product.status == False:
                    raise Exception('Product is disabled')
                
                if detail.quantity > product.stock:
                    raise Exception('Product out of stock')
                
                product.stock -= detail.quantity

                sale_detail = SaleDetailModel(
                    quantity=detail.quantity,
                    price=detail.price,
                    subtotal=detail.subtotal,
                    product_id=product.id
                )
                sale_details.append(sale_detail)

            last_sale = SaleModel.query.order_by(
                SaleModel.id.desc()
            ).first()

            sale_code = 'B-0001'
            if last_sale:
                last_code = last_sale.code
                last_number = int(last_code.split('-')[1])
                new_number = last_number + 1
                sale_code = f'B-{str(new_number).zfill(4)}'

            sale = SaleModel(
                code=sale_code,
                total=validated_data.total,
                customer_id=customer.id,
                sale_details=sale_details
            )

            db.session.add(sale)
            db.session.commit()
            
            return 'Ok', 200
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Unexpected error',
            }, 500