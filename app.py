from wsgi import create_app
from wsgi.myApi.url import myApi
from wsgi.myApi import tests_myapi

app = create_app()

if __name__ == '__main__':
    app.run()
