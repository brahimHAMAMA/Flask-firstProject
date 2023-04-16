import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate


app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = '9ebc4527086c8e21b0da932c941395f85b73e8f908b6cc401be258551f401c72'

basedir = os.path.abspath(os.path.dirname(__file__))

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pythonic.db'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.app_context().push()

bcrypt = Bcrypt(app)


login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from pythonic import routes