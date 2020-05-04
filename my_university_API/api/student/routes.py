# This file contain all routes of student

####################################################################
#                             import
####################################################################
from api.student import student  # to use api
from flask_restx import Resource  # to use Resource, that expose http request method


####################################################################
#                             routing
####################################################################
@student.route('/hello')
class Testing(Resource):
    def get(self):
        return {'Test': '1'}
