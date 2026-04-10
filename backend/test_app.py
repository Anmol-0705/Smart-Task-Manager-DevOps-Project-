from app import app

def test_get_tasks():
    client = app.test_client()
    response = client.get('/tasks')
    assert response.status_code == 200