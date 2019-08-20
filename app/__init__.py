from flask import Flask

app = Flask(__name__)
# tell Flask to read config.py
app.config.from_object('config')

from app import views
