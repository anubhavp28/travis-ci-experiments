from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    
    yield client
    
def test_current_series(client):
    """ Test /series/current API endpoint """
    
    response = client.get('/series/current')
    assert response.is_json == True
