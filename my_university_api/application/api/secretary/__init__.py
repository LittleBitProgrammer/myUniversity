# This file is executed when the secretary module is imported

####################################################################
#                             import
####################################################################
from flask_restx import Namespace  # to use Namespace of flask RESTx

####################################################################
#                         initialization
####################################################################
secretary = Namespace('secretary', description='Secretary related operations')

####################################################################
#                        circular imports
####################################################################
from application.api.secretary import routes
