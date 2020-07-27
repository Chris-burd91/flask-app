# import Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# create a new instance of Flask and store it in app 

app = Flask(__name__)

app.config['SECRET_KEY'] =str(getenv('SECRET_KEY'))
# import the ./application/routes.py file

app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('DATABASE_URI'))
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
from application import routes
