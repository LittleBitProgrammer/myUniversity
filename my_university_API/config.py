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
    # we have a default string
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'TECNOLOGIE_WEB_2020'
