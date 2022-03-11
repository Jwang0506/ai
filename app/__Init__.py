import os
from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = 'you can put any text'

from app import views