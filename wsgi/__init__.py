from flask import Flask
from wsgi.logger import Logger

app = Flask(__name__)

logger_obj = Logger("my_logger")
app_logger = logger_obj.app_logger_obj
