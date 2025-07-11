from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config') # importa as configurações 
    
    db.init_app(app, db)
    migrate.init_app(app, db)

    @app.route('/')
    def home():
        return 'Hello from TaskHub (com app factory)!'
    
    return app