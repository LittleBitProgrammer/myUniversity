# This file contain all routes of professor

####################################################################
#                             import
####################################################################
from api.global_op import global_op  # to use api
from flask_restx import Resource  # to use Resource, that expose http request method


####################################################################
#                             routing
####################################################################
@global_op.route('/hello')
class Testing(Resource):
    def get(self):
        return {'Test': '2'}