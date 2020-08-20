from wsgi import create_app
from wsgi.myApi.url import myApi

app = create_app()

if __name__ == '__main__':
    app.run()
