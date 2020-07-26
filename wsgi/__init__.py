from flask import Flask
from wsgi.logger import Logger
from wsgi.myApi.url import myApi, urls


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.register_blueprint(myApi, url_prefix='/api')
    return app
