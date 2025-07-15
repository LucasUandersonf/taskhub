from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.tasks import tasks_bp  

db = SQLAlchemy() 
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view ='auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    from app.models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from app.auth import auth
    from app.auth import routes
    app.register_blueprint(auth)


    app.register_blueprint(tasks_bp)  # Registra o blueprint de tarefas

    @app.route('/')
    def home():
        return 'Hello from TaskHub (com app factory)!'
    
    return app