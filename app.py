from flask import Flask
from flask_restufl import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hoteis(Resource):
    def get(self):
        return {'hoteis': 'meus hoteis'}

api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True)
