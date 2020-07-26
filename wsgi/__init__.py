from flask import Flask
from wsgi.logger import Logger


def create_app():
    app = Flask(__name__)
    app.debug = True
    from wsgi.myApi.url import myApi, urls
    app.register_blueprint(myApi, url_prefix='/api')
    return app
