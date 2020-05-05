# This file contain all routes of professor

####################################################################
#                             import
####################################################################
from api.global_op import global_op  # to use api
from flask_restx import Resource  # to use Resource, that expose http request method


####################################################################
#                             routing
####################################################################
# ============================    lezioni_corso    ========================== #
@global_op.route('/lezioni_corso')
class Lesson(Resource):

    def post(self):
        return {'lezione': '2'}


# ============================    inserimento contatto (condivisa da studente e docente)   ========================== #
@global_op.route('/contatto')
class Contact(Resource):

    def post(self):
        return {'contatto': '1'}