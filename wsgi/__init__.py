from flask import Flask
from wsgi.logger import Logger
import os

app = Flask(__name__)

logger_obj = Logger("my_logger")
logger_obj.app_logger_obj = os.path.join(os.path.abspath(os.path.curdir), "logs")
app_logger = logger_obj.app_logger_obj
