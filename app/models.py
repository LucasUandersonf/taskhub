from flask_login import UserMixin
from app import db
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64), unique=True, nullable = False)
    password = db.Column(db.String(128), nullable = False)
    tasks = db.relationship('Task', backref='owner', lazy= True)

    def __repr__(self):
        return f'<User {self.username}>'
    

class Task(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text)
    done = db.Column(db.Boolean, default= False)
    timestamp = db.Column(db.DateTime, default = datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Task {self.title}>'

