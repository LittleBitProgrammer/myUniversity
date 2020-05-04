# This file contain all routes of professor

####################################################################
#                             import
####################################################################
from api.professor import professor  # to use api
from flask_restx import Resource  # to use Resource, that expose http request method


####################################################################
#                             routing
####################################################################
@professor.route('/hello')
class Testing(Resource):
    def get(self):
        return {'Test': '2'}