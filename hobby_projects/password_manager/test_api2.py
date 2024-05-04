import json
import pytest
from .app import app

# Define the test data
PASSWORD_FILE = "/Users/shrilc/IdeaProjects/shrilc/batch2/hobby_projects/secrets/test_passwords.json"
TEST_PASSWORDS = {
    "1": {"username": "user1", "password": "password1"},
    "2": {"username": "user2", "password": "password2"},
}


# Define the setup and teardown functions
@pytest.fixture(scope='function')
def client():
    # Create a test app with test database
    app.config['TESTING'] = True
    app.config['PASSWORD_FILE'] = PASSWORD_FILE
    with app.test_client() as client:
        yield client

    # Clean up the test database
    # Note: When file is open with 'w' write mode , contents of the files will be deleted
    with open(PASSWORD_FILE, 'w') as f:
        json.dump({}, f)


# Define the test functions
def test_get_passwords(client):
    with open(PASSWORD_FILE, 'w') as f:
        json.dump(TEST_PASSWORDS, f)

    # Call the get_passwords endpoint
    response = client.get('/passwords')

    assert response.status_code == 200
    assert response.json == TEST_PASSWORDS


def test_get_password(client):
    with open(PASSWORD_FILE, 'w') as f:
        json.dump(TEST_PASSWORDS, f)

    response = client.get('/passwords/1')

    assert response.status_code == 200
    assert response.json == TEST_PASSWORDS["1"]

    # Call the get password for record which is not found
    response = client.get('/passwords/3')
    assert response.status_code == 200
    assert response.json == {"error": "Password not found."}
