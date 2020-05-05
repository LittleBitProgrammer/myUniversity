# This file contain all routes of student

####################################################################
#                             import
####################################################################
from api.student import student  # to use api
from flask_restx import Resource  # to use Resource, that expose http request method


####################################################################
#                             routing
####################################################################
# ============================    studente    ========================== #
@student.route('/login')
class Login(Resource):

    def post(self):
        return {'studente': '1'}


# ============================    update password    ========================== #
@student.route('/password')
class Password(Resource):

    def post(self):
        return {'password': '1'}


# ============================    get contatto   ========================== #
@student.route('/contatti')
class GetContact(Resource):

    def post(self):
        return {'contatti': '1'}


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


# ============================    get discipline   ========================== #
@student.route('/discipline')
class Discipline(Resource):

    def post(self):
        return {'riceve disciplina': '1'}


# ============================    segui disciplina   ========================== #
@student.route('/follow_disciplina')
class FollowDiscipline(Resource):

    def post(self):
        return {'segui disciplina': '1'}


# ============================    unfollow disciplina   ========================== #
@student.route('/unfollow_disciplina')
class UnfollowDiscipline(Resource):

    def post(self):
        return {'segui disciplina': '1'}


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


# ============================    calendario   ========================== #
@student.route('/calendario')
class Calendario(Resource):

    def post(self):
        return {'iscrizione newsletter': '1'}
