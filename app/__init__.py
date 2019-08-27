from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# tell Flask to read config.py
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
