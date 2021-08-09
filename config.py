class Config(object):
    DEBUG = False
    TESTING = False

    IMAGES = "static/img/"

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True