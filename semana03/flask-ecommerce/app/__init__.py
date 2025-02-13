from flask import Flask
from db import db
from flask_migrate import Migrate
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)

from app.routes import api