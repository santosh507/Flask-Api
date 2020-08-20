"""
    Config file for myApi
"""
from flask import current_app


class AppConfig:
    SECRET_KEY = "asdwqfsfxhhgmwef12213543tga121"
    SQLALCHEMY_DATABASE_URI = "sqlite:///myApi.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
