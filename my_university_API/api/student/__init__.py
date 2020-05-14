# This file is executed when the student module is imported

####################################################################
#                             import
####################################################################
from flask_restx import Namespace  # to use Namespace of flask RESTx

####################################################################
#                         initialization
####################################################################
student = Namespace('student', description='Student related operations')

####################################################################
#                        circular imports
####################################################################
from api.student import routes
# Qui si trovano le routes part 2 dello studente
# from api.student import routes_charlie
