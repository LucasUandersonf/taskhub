import os
from flask import Flask
import config
from extensions import db, login_manager, migrate
 
login_manager.login_view ='auth.login'

def create_app():
    app = Flask(__name__)

    env = os.environ.get("FLASK_ENV", "development")
    if env == "production":
        app.config.from_object(config.ProductionConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)
    
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
    app.register_blueprint(tasks_bp)  

   
    
    return app