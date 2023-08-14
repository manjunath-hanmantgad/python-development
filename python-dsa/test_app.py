import json
import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_generate_array_success(client):
    data = {"sentence": "This is an example sentence"}
    response = client.post('/generate_array', json=data)
    assert response.status_code == 200
    result = json.loads(response.data)
    assert isinstance(result, list)
    assert len(result) == 500

def test_generate_array_invalid_input(client):
    data = {"sentence": 123}  # Invalid input, expecting a string
    response = client.post('/generate_array', json=data)
    assert response.status_code == 400
    result = json.loads(response.data)
    assert 'error' in result

def test_generate_array_server_error(client):
    # Simulate a server error by sending an invalid JSON payload
    response = client.post('/generate_array', data="invalid json data")
    assert response.status_code == 500
    result = json.loads(response.data)
    assert 'error' in result

if __name__ == '__main__':
    pytest.main()
