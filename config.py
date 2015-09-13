from os import getenv, \
               path
from time import time
from datetime import timedelta


class Config(object):
    CACHE_BUSTER = int(path.getmtime(__file__))
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
    REMEMBER_COOKIE_DURATION = timedelta(days=30)
    SECRET_KEY = getenv('SECRET_KEY')
    SEND_FILE_MAX_AGE_DEFAULT = 365 * 86400
    SITE_NAME = getenv('SITE_NAME', 'Flask Boilerplate')
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL').replace('mysql2:', 'mysql:')
    SQLALCHEMY_ECHO = getenv('SQLALCHEMY_ECHO', False)


class ProductionConfig(Config):
    DEBUG = getenv('DEBUG', False)
    TESTING = False


class DevelopmentConfig(Config):
    CACHE_BUSTER = int(time())
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
