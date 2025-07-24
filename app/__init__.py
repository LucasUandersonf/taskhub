from flask import Flask
from config import Config
from extensions import db, login_manager, migrate
 
login_manager.login_view ='auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
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

    from app.tasks import tasks_bp 
    from app.tasks import routes
    app.register_blueprint(tasks_bp)  # Registra o blueprint de tarefas

   
    
    return app