# Django Rest Framework

## Instalación

```bash
pip install django
pip install djangorestframework
pip install python-dotenv
pip install psycopg2-binary
```

## Creación del proyecto

```bash
django-admin startproject django_restframework .
```

## Configuración

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    ...
]
```

## Configuración de la base de datos

### Creación de las variables de entorno `.env`

```bash
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
DB_PORT=''
```