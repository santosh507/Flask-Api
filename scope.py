from flask import Flask
from myApi.url.urls import myApi

scope = Flask(__name__)

scope.register_blueprint(myApi,url_prefix='/api')
scope.debug = True

if __name__ == '__main__':
    scope.run()
