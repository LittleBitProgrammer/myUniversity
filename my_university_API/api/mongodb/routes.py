# This file contain all routes of mongodb

####################################################################
#                             import
####################################################################

from flask_restx import Resource, reqparse, fields  # to use Resource, that expose http request method
from api.mongodb.mongo_functions import *
from api.mongodb.models import *


####################################################################
#                             routing
####################################################################
# ============================    login    ========================== #
@mongodb.route('/send_msg')
class Send_msg(Resource):
    def get(self):
        return returnHelloWorld()