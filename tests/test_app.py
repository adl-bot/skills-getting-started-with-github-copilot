from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Example test for root endpoint using AAA pattern

def test_read_root():
    # Arrange
    # (No setup needed for this endpoint)

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# Add more tests for other endpoints following AAA pattern
