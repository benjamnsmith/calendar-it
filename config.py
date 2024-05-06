from os import environ
class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY') or '1E7456C6516D6B3224BC3BA2'

