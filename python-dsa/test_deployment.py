import random
import requests
import pytest
from app import app

# Set up the base URL for the running server
BASE_URL = "http://127.0.0.1:5000"

@pytest.fixture(scope='module')
def client():
    # Start the Flask app in testing mode
    app.testing = True
    with app.test_client() as client:
        yield client

def test_generate_array_success(client):
    data = {"sentence": "This is an example sentence"}
    response = client.post('/generate_array', json=data)
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, list)
    assert len(result) == 500

def test_generate_array_invalid_input(client):
    data = {"sentence": 123}  # Invalid input, expecting a string
    response = client.post('/generate_array', json=data)
    assert response.status_code == 400
    result = response.json()
    assert 'error' in result

def test_generate_array_server_error(client):
    # Simulate a server error by sending an invalid JSON payload
    response = client.post('/generate_array', data="invalid json data")
    assert response.status_code == 500
    result = response.json()
    assert 'error' in result

def test_deployment():
    # Test the running server by making actual HTTP requests
    data = {"sentence": "This is an example sentence"}
    response = requests.post(f"{BASE_URL}/generate_array", json=data)
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, list)
    assert len(result) == 500

if __name__ == '__main__':
    pytest.main()
