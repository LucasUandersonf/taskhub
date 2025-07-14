from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.models import User, db
from app.forms import LoginForms, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from app.auth import auth


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForms()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
    