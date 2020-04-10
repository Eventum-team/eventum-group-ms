from flask import Flask
from models import db
from models import config

# Crate a new flask aplication
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Bind database to app context 
app.app_context().push()
db.init_app(app)

# Create tables 
db.create_all()

# routes
import resources.GroupTypeResource
import resources.GroupResource