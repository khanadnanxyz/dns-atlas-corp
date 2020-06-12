import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'atlas-dns-service-key'
    '''
    Considering SectorID is fixed, but keeping it configurable
    and we are deploying it for Sector 1
    '''
    SECTOR_ID = os.environ.get('SECTOR_ID', 1)


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
