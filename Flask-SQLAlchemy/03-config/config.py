import os


class Configuration(object):
    DEBUG = True
    
    # SQLAlchemy 설정
    APPLICATION_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/app.db' % APPLICATION_DIR    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
