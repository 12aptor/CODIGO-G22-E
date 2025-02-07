from flask import Flask
from db import db
from flask_migrate import Migrate

app = Flask(__name__)
db.init_app(app)
migrate = Migrate(app, db)