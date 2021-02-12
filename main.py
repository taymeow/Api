from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
# wrapping app in restful api
api = Api(app) 

# inheriting from resource and making a class that is Resource
class HelloWorld(Resource): 
    def get(self):
        # returns python dictionary, need to make this a key value pair
        # when we return information from api we need to make sure its serializable. returning json serializable objects
        return{"name": name, "test": test}

# registers class as a resource, / is default url
# want user to type string after helloworld. passing string param.
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")


if __name__ == "__main__":
    app.run(debug=True)
