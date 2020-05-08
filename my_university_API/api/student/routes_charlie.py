# This file contain all routes of student (This file is for Charlie)

####################################################################
#                             import
####################################################################
from api.student import student  # to use api
from flask_restx import Resource, reqparse, fields  # to use Resource, that expose http request method
import mysql.connector
from mysql.connector import Error


# ============================    richiesta ricevimento   ========================== #
@student.route('/richiesta_ricevimento')
class RequestReceipt(Resource):

    def post(self):
        return {'richiesta_ricevimento': '1'}


# ============================    cancella ricevimento   ========================== #
@student.route('/cancella_richiesta_ricevimento')
class DelRequestReceipt(Resource):

    def post(self):
        return {'richiesta_ricevimento': '1'}

# ============================    iscrizione_newletter   ========================== #
@student.route('/iscrizione')
class SubmitNewsletter(Resource):

    def post(self):
        return {'iscrizione newsletter': '1'}

# ============================    avvisi   ========================== #
@student.route('/avvisi')
class SubmitNewsletter(Resource):

    def post(self):
        return {'iscrizione newsletter': '1'}