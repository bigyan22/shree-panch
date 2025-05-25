from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
app= Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = '907fc3c7d13cbd71505d5b7fd2e3d754'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)


from Main import routes
migrate = Migrate(app, db)

