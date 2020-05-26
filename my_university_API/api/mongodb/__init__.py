# This file is executed when the professor module is imported

####################################################################
#                             import
####################################################################
from flask_restx import Namespace  # to use Namespace of flask RESTx

####################################################################
#                         initialization
####################################################################
mongodb = Namespace('mongodb', description='MongoDB related operations')

####################################################################
#                        circular imports
####################################################################
from api.mongodb import routes


