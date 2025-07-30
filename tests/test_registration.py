import pytest
from utils.data_factory import generate_valid_registration_data, generate_invalid_registration_data
import time

@pytest.mark.smoke
def test_registration_smoke(api_client, logger):
    """Smoke test: Register a new user."""
    user_data = generate_valid_registration_data()
    
    # Register user
    response = api_client.users.register_user(user_data)
    assert response.status_code == 200, f"Registration failed! Expected 200, got {response.status_code}"
    
    logger.info(f"Registration successful for user: {user_data.username}")


@pytest.mark.functional
def test_registration_functional(api_client, logger):
    """Functional test: Complete registration flow with login and validation."""
    user_data = generate_valid_registration_data()
    
    # Register user
    response = api_client.users.register_user(user_data)
    assert response.status_code == 200, f"Registration failed! Expected 200, got {response.status_code}"

    # Try to login
    login_response = api_client.users.login_user(user_data.username, user_data.password)
    assert login_response.status_code == 200, f"Login failed! Expected 200, got {login_response.status_code}"

    # Username should be taken after registration
    username_available_after = api_client.users.validate_username(user_data.username)
    logger.info(f"Username '{user_data.username}' available after registration: {username_available_after}")
    assert username_available_after == False, f"Username should be taken after registration, but validateUserName returned {username_available_after}"

@pytest.mark.negative
def test_registration_negative(api_client, logger):
    """Negative test: Register with invalid password format."""
    user_data = generate_invalid_registration_data()
    logger.info(f"Testing registration with invalid password for user: {user_data.username} ({user_data.firstName} {user_data.lastName})")
    
    # Check if username is available before registration
    username_available_before = api_client.users.validate_username(user_data.username)
    assert username_available_before == True, f"Username should be available before registration, but validateUserName returned {username_available_before}"
    
    # Try to register user
    response = api_client.users.register_user(user_data)
    assert response.status_code == 400, f"Expected 400 for invalid password, got {response.status_code}"

   