import pytest
from utils.data_factory import generate_valid_registration_data, generate_invalid_registration_data

@pytest.mark.smoke
def test_registration_smoke(api_client, logger):
    """Smoke test: Register a new user with realistic data."""
    user_data = generate_valid_registration_data()
    logger.info(f"Testing registration for user: {user_data.username} ({user_data.firstName} {user_data.lastName})")
    
    response = api_client.users.register_user(user_data)
    
    # Check status code
    assert response.status_code == 200, f"Registration failed! Expected 200, got {response.status_code}"
    
    logger.info("Registration successful!")

def test_registration_invalid_password(api_client, logger):
    """Negative test: Register with invalid password format."""
    user_data = generate_invalid_registration_data()
    logger.info(f"Testing registration with invalid password for user: {user_data.username} ({user_data.firstName} {user_data.lastName})")
    
    response = api_client.users.register_user(user_data)
    
    # Check status code
    assert response.status_code == 400, f"Expected 400 for invalid password, got {response.status_code}"
    
    logger.info("Invalid password correctly rejected!")

   