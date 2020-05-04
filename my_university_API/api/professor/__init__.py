# This file is executed when the professor module is imported

####################################################################
#                             import
####################################################################
from flask_restx import Namespace  # to use Namespace of flask RESTx

####################################################################
#                         initialization
####################################################################
professor = Namespace('professor', description='Professor related operations')

####################################################################
#                        circular imports
####################################################################
from api.professor import routes
