import pandas as pd
from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast


app = Flask(__name__)
api= Api(app)
class Users(Resource):
    
    
    pass



class Locations(Resource):
    
    
    pass

api.add_resource(Users, '\Users')
api.add_resource(Locations, '\Locations')



