from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.models import User, db
from app.forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from app.auth import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('home'))
        flash('Usuário ou senha inválidos', 'danger')
    return render_template('auth/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        flash('Usuário criado! Faça login.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'info')
    return redirect(url_for('auth.login'))