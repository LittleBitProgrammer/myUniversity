# This file is executed when the api module is imported

####################################################################
#                             import
####################################################################
from flask_restx import Api  # to use flask-restx lib
from application.api.secretary import secretary  # to use secretary namespace
from application.api.professor import professor  # to use professor namespace
from application.api.student import student  # to use student namespace
from application.api.mongodb import mongodb
from flask_cors import CORS

from flask import Blueprint
api_blueprint = Blueprint('api', __name__)

####################################################################
#                           api_variables
####################################################################
api_version = '0.1'  # version of our API
api_title = 'myUniversity API'  # title of our API
api_doc = '/'  # doc path of our API
api_license = 'Apache-2.0'  # license name of our API
api_license_url = 'https://github.com/robertove93/myUniversity/blob/master/LICENSE'  # license url of our API
api_contact_email = 'roberto.vecchio001@studenti.uniparthenope.it'  # default contact (it's a placeholder)
api_prefix = f'/{api_version}/'  # base url of our API
api_description = 'This is myUniversity Official API. We divided the API in three main category:' \
                  '\n- Secretary' \
                  '\n- Professor' \
                  '\n- Student '  \
                  '\n- Mongodb '  # description of our API
api_contact = '[carlo.lomello001@studenti.uniparthenope.it]  -  ' \
              '[francesco.mabilia001@studenti.uniparthenope.it]  -  ' \
              '[roberto.vecchio001@studenti.uniparthenope.it]'  # contact of our team

####################################################################
#                       object initialization
####################################################################

# Use CORS
CORS(api_blueprint)

# Creation of a Api object
api = Api(api_blueprint,
          version=api_version,
          title=api_title,
          doc=api_doc,  # TODO: web page of documentation
          description=api_description,
          license=api_license,
          license_url=api_license_url,
          contact=api_contact,
          contact_email=api_contact_email,
          prefix=api_prefix,
          catch_all_404=True)

####################################################################
#                           Namespace
####################################################################
api.add_namespace(secretary)
api.add_namespace(professor)
api.add_namespace(student)
api.add_namespace(mongodb)

####################################################################
#                        circular imports
####################################################################
