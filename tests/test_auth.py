from app import create_app

def test_register_page(client):
    response = client.get('/register')
    assert response.status_code == 200
    assert "Cadastrar" in response.get_data(as_text=True)


from app.models import User
from extensions import db 
from werkzeug.security import generate_password_hash

def test_login(client, app):
    with app.app_context():
        user = User(username = "lucas@example.com", password = generate_password_hash("123456"))
        db.session.add(user)
        db.session.commit()

    response = client.post("/", data = {
        'username': 'lucas@example.com',
        'password': '123456'
    }, follow_redirects = True)

    assert response.status_code == 200
    assert 'TaskHub' in response.get_data(as_text=True)



def test_login_incorreto(client, app):
    with app.app_context():
        user = User(username = "lucas@example.com", password = generate_password_hash("123456"))
        db.session.add(user)
        db.session.commit()

    response = client.post("/", data = { 
        'username' : 'lucas@example.com',
        'password' : 'errada'
    }, follow_redirects = True)

    assert 'Usuario ou senha invalidos' in response.get_data(as_text=True)


def test_logout(client, app):
    with app.app_context():
        user = User(username = "lucas@example.com", password = generate_password_hash("123456"))
        db.session.add(user)
        db.session.commit()

    client.post("/", data = {
        'username':'lucas@example.com',
        'password': '123456'
    }, follow_redirects = True)

    response = client.get('/logout', follow_redirects = True) 

    assert b'Sair' not in response.data
    assert b'Entrar' in response.data