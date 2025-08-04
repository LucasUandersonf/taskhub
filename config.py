import os 

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config: 
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'segredo-desenvolvimento'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = False
    




