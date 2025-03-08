from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    AppointmentSerializer,
)
from django.db import transaction
import requests
import os
from .models import (
    AppointmentModel,
    PaymentModel,
)
from datetime import datetime

class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer

    def create(self, request):
        with transaction.atomic():
            response = super().create(request)

            return Response({
                'object': 'create_appointment',
                'data': response.data
            }, status=status.HTTP_200_OK)

class PaymentCreateView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            appointment_id = kwargs.get('appointment_id')

            appointment = AppointmentModel.objects.get(id=appointment_id)

            if not appointment:
                raise Exception('Appointment not found')

            servicios = [
                {
                    'price': appointment.service.price,
                    'quantity': 1,
                    'total': appointment.service.price, # price * quantity
                }
            ]

            items = []
            for service in servicios:
                precio_servicio = service['price']
                total = service['price'] * service['quantity']
                valor_unitario = precio_servicio / 1.18
                subtotal = total / 1.18
                igv = total - subtotal

                item = {
                    'unidad_de_medida': 'ZZ',
                    'codigo': 'S-001',
                    'descripcion': 'Corte de pelo',
                    'cantidad': 1,
                    'valor_unitario': valor_unitario,
                    'precio_unitario': precio_servicio,
                    'subtotal': subtotal,
                    'tipo_de_igv': 1,
                    'igv': igv,
                    'total': total,
                    'anticipo_regularizacion': False,
                }

                items.append(item)

            total = appointment.service.price
            subtotal = total / 1.18
            igv = total - subtotal

            invoice_data = {
                'operacion': 'generar_comprobante',
                'tipo_de_comprobante': 2,
                'serie': 'BBB1',
                'numero': 1,
                'sunat_transaction': 1,
                'cliente_tipo_de_documento': 1,
                'cliente_numero_de_documento': appointment.customer.document_number,
                'cliente_denominacion': appointment.customer.name,
                'cliente_direccion': appointment.customer.address,
                'cliente_email': appointment.customer.email,
                'fecha_de_emision': datetime.now().strftime('%d-%m-%Y'),
                'moneda': 1,
                'porcentaje_de_igv': 18.0,
                'total_gravada': subtotal,
                'total_igv': igv,
                'total': total,
                'enviar_automaticamente_a_la_sunat': True,
                'enviar_automaticamente_al_cliente': True,
                'items': items,
            }

            response = requests.post(
                url='https://api.nubefact.com/api/v1/99ae592e-9d4e-4961-84be-dac68239b909',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {os.getenv('NF_API_KEY')}'
                },
                json=invoice_data
            )

            response_json = response.json()
            response_status = response.status_code

            if response_status != 200:
                raise Exception(response_json['errors'])
            
            payment = PaymentModel.objects.create(
                amount=appointment.service.price,
                payment_method='YAPE',
                payment_date=datetime.now(),
                appointment=appointment,
            )
            payment.save()
            
            return Response({
                'object': 'create_payment',
                'data': response_json
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'object': 'create_payment',
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)