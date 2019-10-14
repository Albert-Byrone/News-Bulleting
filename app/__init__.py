from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

app = Flask(__name__)

from app import views