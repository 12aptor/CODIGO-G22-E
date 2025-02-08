from flask import Flask
from db import db
from flask_migrate import Migrate
from config import DevelopmentConfig

from app.models import (
    category_model,
    customer_model,
    product_model,
    role_model,
    sale_detail_model,
    sale_model,
    update_product_logs_model,
    user_model
)

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
