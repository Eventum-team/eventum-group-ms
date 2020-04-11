from flask import Flask
from models import db
from models import config

app = Flask(__name__)

# Bind database to application context 
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db.init_app(app)

# Create tables 
db.create_all()

# errors
import resources.errorHandlers

# routes
import resources.GroupTypeResource
import resources.GroupResource