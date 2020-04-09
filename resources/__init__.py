from flask import Flask
from models import db
from models import config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db.init_app(app)
db.create_all()


import resources.catResource