# This file is executed when the api module is imported

####################################################################
#                             import
####################################################################
from flask import Flask  # to use flask Framework
from flask_restx import Api  # to use flask-restx lib

####################################################################
#                       object initialization
####################################################################
# Creation of a Flask object
app = Flask(__name__)
# Creation of a Api object
api = Api(app,
          version='0.1',
          title='myUniversity API',
          description='This is myUniversity Official API. We divided the API in three main category:'
                      '\n- Secretary'
                      '\n- Professor'
                      '\n- Student ',
          license='Apache-2.0',
          license_url='https://github.com/robertove93/myUniversity/blob/master/LICENSE',
          contact='[carlo.lomello001@studenti.uniparthenope.it]  -  '
                  '[francesco.mabilia001@studenti.uniparthenope.it]  -  '
                  '[roberto.vecchio001@studenti.uniparthenope.it]',
          contact_email='roberto.vecchio001@studenti.uniparthenope.it',
          catch_all_404s=True)


from api import routes
