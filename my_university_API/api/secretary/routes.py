# This file contain all routes of secretary

####################################################################
#                             import
####################################################################
from api.secretary import secretary  # to use api
from flask_restx import Resource  # to use Resource, that expose http request method


####################################################################
#                             routing
####################################################################
@secretary.route('/hello')
class Testing(Resource):
    def get(self):
        return {'Test': '2'}