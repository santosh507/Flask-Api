from wsgi import app
from wsgi.myApi.url.urls import myApi

app.register_blueprint(myApi, url_prefix='/api')
app.debug = True

if __name__ == '__main__':
    app.run()
