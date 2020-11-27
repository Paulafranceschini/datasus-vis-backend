import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = ''
    #SQLALCHEMY_DATABASE_URI ="postgres+pg8000:///postgres:0yEIpgye8jvEd9rq@tcc-datasus?unix_sock=cloudsql/tcc-datasus-289918:us-central1:tcc-datasus-postgres/.s.PGSQL.5432"
    #SQLALCHEMY_DATABASE_URI = os.environ['postgresql:///postgres:0yEIpgye8jvEd9rq@34.70.225.26:5432/tcc-datasus']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True