from app import create_app

def test_register_page(client):
    response = client.get('/register')
    assert response.status_code == 200
    assert b"Cadastrar" in response.data