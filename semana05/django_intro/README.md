# Django Intro

## Instalación

```bash
pip install django
```
## Crear la carpeta del proyecto

```bash
mkdir django_intro
cd django_intro
```

## Crear un proyecto

```bash
django-admin startproject django_intro .
```

## Iniciar el servidor

```bash
python manage.py runserver
```

## Migraciones

```bash
python manage.py makemigrations # Crea las migraciones
python manage.py migrate # Ejecuta las migraciones
python manage.py showmigrations # Muestra las migraciones
```

## Crear un superusuario

```bash
python manage.py createsuperuser
```