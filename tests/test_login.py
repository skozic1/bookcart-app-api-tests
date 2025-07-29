import pytest
from utils.data_factory import get_valid_user_credentials, get_invalid_user_credentials

@pytest.mark.smoke
def test_login_smoke(api_client, logger):
    """Smoke test: Login with valid user and verify all response fields."""
    user_credentials = get_valid_user_credentials()
    logger.info(f"Testing login for user: {user_credentials['username']}")
    
    response = api_client.users.login_user(
        username=user_credentials["username"],
        password=user_credentials["password"]
    )
    
    # Check status code
    assert response.status_code == 200, f"Login failed! Expected 200, got {response.status_code}"
    
    # Check response structure
    response_data = response.json()
    assert "token" in response_data, "Response should contain authentication token"
    assert "userDetails" in response_data, "Response should contain userDetails"
    
    # Verify user details
    user_details = response_data["userDetails"]
    assert user_details["username"] == user_credentials["username"], \
        f"Username mismatch: expected {user_credentials['username']}, got {user_details['username']}"
    assert user_details["userId"] == user_credentials["userId"], \
        f"UserId mismatch: expected {user_credentials['userId']}, got {user_details['userId']}"
    assert user_details["userTypeName"] == user_credentials["userTypeName"], \
        f"UserTypeName mismatch: expected {user_credentials['userTypeName']}, got {user_details['userTypeName']}"
    
    # Verify token is not empty
    assert response_data["token"], "Authentication token should not be empty"
    
    logger.info(f"Login successful! User: {user_details['username']}")

def test_login_invalid_password(api_client, logger):
    """Negative test: Login with invalid password."""
    user_credentials = get_invalid_user_credentials()
    logger.info(f"Testing login with invalid password for user: {user_credentials['username']}")
    
    response = api_client.users.login_user(
        username=user_credentials["username"],
        password=user_credentials["password"]
    )
    
    # Check status code
    assert response.status_code == 401, f"Expected 401 for invalid password, got {response.status_code}"
    
    logger.info("Invalid password correctly rejected!")