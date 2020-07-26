from wsgi import create_app

scope = create_app()
if __name__ == '__main__':
    scope.run()
