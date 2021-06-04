import os


class Config():
    DEBUG = os.getenv('FLASK_DEBUG', default=False)
    ENV = os.getenv('FLASK_ENV', default='production')

    ALMA_SRU = os.getenv('ALMA_SRU')
    PRIMO_URL = os.getenv('PRIMO_URL')
    TARGET_URL = os.getenv('TARGET_URL')


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    ENV = 'testing'

    ALMA_SRU = 'https://mit.alma.exlibrisgroup.com/view/sru/01MIT_INST?version=1.2&operation=searchRetrieve&recordSchema=dc&query=alma.all_for_ui='
    PRIMO_URL = 'http://example.com/primo/'
    TARGET_URL = 'http://example.com/hallo/'
