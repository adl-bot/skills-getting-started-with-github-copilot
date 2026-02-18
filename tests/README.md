# Backend FastAPI Tests

This directory contains tests for the FastAPI backend, structured using the Arrange-Act-Assert (AAA) pattern and run with pytest.

## Structure
- `test_app.py`: Tests FastAPI endpoints using TestClient and AAA pattern.
- `__init__.py`: Marks this directory as a Python package.

## Running Tests
Install dependencies from requirements.txt, then run:

    pytest

## AAA Pattern
Each test is structured as:
- **Arrange:** Setup test data and environment
- **Act:** Execute the action (e.g., HTTP request)
- **Assert:** Validate the response and side effects
