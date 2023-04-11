import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = '9ebc4527086c8e21b0da932c941395f85b73e8f908b6cc401be258551f401c72'

basedir = os.path.abspath(os.path.dirname(__file__))

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pythonic.db'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
app.app_context().push()

from pythonic import routes