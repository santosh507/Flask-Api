from flask import Flask
from wsgi.logger import Logger
from flask_sqlalchemy import SQLAlchemy
from wsgi.myApi.config import AppConfig

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(AppConfig)
    db.init_app(app)
    # Create Tables
    from wsgi.myApi.models import Employee
    db.create_all(app=app)
    # Import Blueprint Routes
    from wsgi.myApi.url import myApi, urls
    app.register_blueprint(myApi, url_prefix='/api')
    return app
