# This file is executed when the api module is imported

####################################################################
#                             import
####################################################################
from flask import Flask  # to use flask Framework
from flask_restx import Api  # to use flask-restx lib
from api.secretary import secretary  # to use student namespace
from api.professor import professor  # to use student namespace
from api.student import student  # to use student namespace

####################################################################
#                           api_variables
####################################################################
version_api = '0.1'

####################################################################
#                       object initialization
####################################################################
# Creation of a Flask object
app = Flask(__name__)
# Creation of a Api object
api = Api(app,
          version=f'{version_api}',
          title='myUniversity API',
          doc='/',  # TODO: web page of documentation
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
          prefix=f'/api/v{version_api}/',
          catch_all_404=True)

####################################################################
#                           Namespace
####################################################################
api.add_namespace(secretary)
api.add_namespace(professor)
api.add_namespace(student)

####################################################################
#                        circular imports
####################################################################
