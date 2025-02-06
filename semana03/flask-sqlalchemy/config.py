import os

class Config:
    # Configuración general
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')

class ProductionConfig(Config):
    # Configuración de producción
    DEBUG = False

class DevelopmentConfig(Config):
    # Configuración de desarrollo
    DEBUG = True

class TestingConfig(Config):
    # Configuración de desarrollo
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'