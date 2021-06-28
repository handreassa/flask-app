from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

app = Flask(__name__)
bootstrap = Bootstrap(app)
login = LoginManager(app)
# Feature that forces user to be redirected to the login page before they view some pages
login.login_view = "login"

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
