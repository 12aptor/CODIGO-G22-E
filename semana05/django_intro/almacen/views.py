from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ProductModel
import datetime

def index(request):
    return HttpResponse('Hola Django 👻')

def date(request):
    now = datetime.datetime.now()
    html = f'<html><body>Ahora es: {now}</body></html>'
    return HttpResponse(html)

def json(request):
    data = {
        'nombre': 'Pepito'
    }
    return JsonResponse(data)

def product(request, id):
    product = ProductModel.objects.get(id=id)
    return render(
        request,
        'product.html',
        context={
            'name': product.name
        }
    )