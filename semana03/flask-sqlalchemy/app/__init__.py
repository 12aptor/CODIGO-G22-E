from flask import Flask
from db import db
from dotenv import load_dotenv
from config import DevelopmentConfig

load_dotenv()

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)

from app.routes import api