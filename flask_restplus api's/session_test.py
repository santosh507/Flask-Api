from flask import Flask, session
from flask_restful import Resource, Api
from inspect import stack

class Visits(Resource):
    def get(self):
        print('{0}.{1}'.format(self.__class__.__name__, stack()[0][3]))
        if 'visits' in session:
            session['visits'] = session['visits'] + 1
        else:
            session['visits']= 1
        print(session.items())
        return "Todays visits : {0}".format(session['visits'])

app = Flask(__name__)
rest = Api(app)

rest.add_resource(Visits,'/visits')

if __name__ == '__main__':
    app.config['SECRET_KEY']="asdwqeqrvsgfgj@!3241"
    app.run(debug=True)
