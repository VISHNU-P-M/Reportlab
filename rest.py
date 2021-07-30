from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'data':'hello'}
    
    def post(self):
        resp = request.get_json()
        print(resp['data'])

api.add_resource(HelloWorld, '/hello-world')

if __name__ == '__main__':
    app.run(debug=True)