from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
# wrapping app in restful api
api = Api(app) 

# inheriting from resource and making a class that is Resource
class HelloWorld(Resource): 
    def get(self):
        # returns python dictionary
        return{"Hellow World"}

# registers class as a resource, / is default url
api.add_resource(HelloWorld, "/helloworld")


if __name__ == "__main__":
    app.run(debug=True)
