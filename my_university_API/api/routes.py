# This file contain all routes of our api

####################################################################
#                             import
####################################################################
from api import api
from flask_restx import Resource

####################################################################
#                             routes
####################################################################
@api.route('/hello')
class Hello(Resource):
    def get(self):
        return {'hello': 'world'}
