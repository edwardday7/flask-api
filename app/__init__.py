from flask import Flask

app = Flask(__name__)

from app import bot
from app import api