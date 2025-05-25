from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
import os
from dotenv import load_dotenv
load_dotenv()
app.config['SECRET_KEY'] = '57bbfe3952f5d6871ff495ec'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)
from flask_migrate import Migrate


from Main import routes
migrate = Migrate(app, db)