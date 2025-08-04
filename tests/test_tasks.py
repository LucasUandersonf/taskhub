import pytest
from app import create_app
from app.models import User, Task
from extensions import db
from werkzeug.security import generate_password_hash


def test_create_task(client, app):
     
    with app.app_context():
        user = User(username = "lucas@example.com", password = generate_password_hash("123456"))
        db.session.add(user)
        db.session.commit()
    
    
    client.post('/', data = {
        'username': 'lucas@example.com',
        'password': '123456'
    }, follow_redirects = True)
    
    response = client.post('/tasks/create', data = {
        'title': 'Estudar Python',
        'description': 'Aprender Flask detalhadamente'
    }, follow_redirects = True)
    
     
    assert 'tarefa criada com sucesso!' in response.get_data(as_text=True)
    
     
    with app.app_context():
        task = Task.query.filter_by(title = 'Estudar Python').first()
        assert task is not None


def teste_create_task_nao_logado(client):
    response = client.post('/tasks/create', data={
        'title': 'Hackear tudo',
        'description': 'Sem login mesmo'
    }, follow_redirects=True)  
    assert  'Login - TaskHub' in response.get_data(as_text=True)


def test_update_task(client, app):
    with app.app_context():
        user = User(username="lucas@example.com", password=generate_password_hash("123456"))
        db.session.add(user)
        db.session.commit()
        task = Task(title="Tarefa antiga", description="desc", user_id=user.id)
        db.session.add(task)
        db.session.commit()

        task_id = task.id  

    client.post('/', data={
        'username': 'lucas@example.com',
        'password': '123456'
    }, follow_redirects=True)

    response = client.post(f'/tasks/{task_id}/edit', data={
        'title': 'tarefa atualizada',
        'description': 'Nova descrição'
    }, follow_redirects=True)

    assert 'Tarefa atualizada com sucesso!' in response.get_data(as_text=True)


def test_delete_task(client, app):
    with app.app_context():
        user = User(username= "lucas@example.com", password=generate_password_hash("123456"))
        db.session.add(user)
        db.session.commit()

        task = Task(title='Apagar essa', description='desc', user_id=user.id)
        db.session.add(task)
        db.session.commit()

        task_id = task.id

    # Login
    client.post('/', data={
        'username': 'lucas@example.com',
        'password': '123456'
    }, follow_redirects=True)

    # Deleta a tarefa
    response = client.post(f'/tasks/{task_id}/delete', follow_redirects=True)

    assert 'Tarefa excluida com sucesso!' in response.get_data(as_text=True)
    with app.app_context():
        deleted = Task.query.get(task.id)
        assert deleted is None


