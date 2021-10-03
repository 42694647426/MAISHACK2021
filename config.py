class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "secret key"


class DevelopmentConfig(Config):
    DEBUG = True
