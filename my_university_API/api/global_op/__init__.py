# This file is executed when the global_op module is imported

####################################################################
#                             import
####################################################################
from flask_restx import Namespace  # to use Namespace of flask RESTx

####################################################################
#                         initialization
####################################################################
global_op = Namespace('universal', description='Multi related operations')

####################################################################
#                        circular imports
####################################################################
from api.global_op import routes
