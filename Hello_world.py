from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

class HelloWorld(Resource):
    def get(self):
        return ("This is my first API program")

api.add_resource(HelloWorld,'/test')

if __name__=='__main__':
    app.run(debug=True)