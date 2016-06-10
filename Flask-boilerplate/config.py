import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

HOST = '127.0.0.1'
PORT = 5000

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/app.db' % BASE_DIR
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
