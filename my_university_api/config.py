# This file contain the configuration of our API

####################################################################
#                             import
####################################################################
import os  # OS routines for NT or Posix depending on what system we're on

####################################################################
#                             class
####################################################################
class Config(object):
    # Set the secret key of our api, if is present it is taken from the environment, in the other case
    # we have a default string. This is used because various lib use this to work
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'TECNOLOGIE_WEB_2020'
    SWAGGER_UI_DOC_EXPANSION = os.environ.get('SWAGGER_UI_DOC_EXPANSION') or 'none'
    SWAGGER_UI_REQUEST_DURATION = os.environ.get('SWAGGER_UI_REQUEST_DURATION') or True
