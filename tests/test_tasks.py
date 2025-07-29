from app.models import User, Task
from extensions import db
from werkzeug.security import generate_password_hash


def test_create_task(client, app):
    # Criar um usuario manualmente no banco 
    with app.app_context():
        user = User(username = "lucas", email = "lucas@example.com", password = generate_password_hash("123456"))
        db.session.add(user)
        db.session.commit()
    
    # Faz login com o usuario criado 
    client.post('/login', data = {
        'email': 'lucas@example.com',
        'password': '123456'
    }, follow_redirects = True)
    
    response = client.post('/create', data = {
        'title': 'Estudar Python',
        'description': 'Aprender Flask detalhadamente'
    }, follow_redirects = True)
    
    # Verifica se a mensagem de sucesso apareceu 
    assert b'Tarefa criada com sucesso' in response.data
    
    # Verifica se a taefa foi salva no banco 
    with app.app_context():
        task = Task.query.filter_by(title = 'Estudar Python').first()
        assert task is not None


def teste_create_task_nao_logado(client):
    response = client.post('/create', data={
        'title': 'Hackear tudo',
        'description': 'Sem login mesmo'
    }, follow_redirects=True)  # <-- CORRETO
    
    assert  b'Voce precisa estar logado' in response.get_data(as_text=True)
