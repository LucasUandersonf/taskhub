from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .models import User
from app.auth import auth

login_manager = LoginManager()
db = SQLAlchemy() 
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
   
    
    app.config.from_object('config.Config') # importa as configurações 
    db.init_app(app)
    migrate.init_app(app, db)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    

    @app.route('/')
    def home():
        return 'Hello from TaskHub (com app factory)!'
    
    return app