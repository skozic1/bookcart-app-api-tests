import pytest
import logging
from utils.api_client import BookCartClient
from utils.data_factory import get_valid_user_credentials

def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://bookcart.azurewebsites.net/api",
        help="Base URL for the Book Cart API"
    )

@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url") 

@pytest.fixture
def api_client(base_url):
    return BookCartClient(base_url)

@pytest.fixture
def logger():
    """Logger fixture for all tests."""
    return logging.getLogger(__name__)

@pytest.fixture
def auth_credentials(api_client):
    """Get authentication credentials (token and user_id) for all tests."""
    user_credentials = get_valid_user_credentials()
    response = api_client.users.login_user(
        username=user_credentials["username"],
        password=user_credentials["password"]
    )
    return {
        "token": response.json()["token"],
        "user_id": user_credentials["userId"]
    }

@pytest.fixture
def user_id(auth_credentials):
    """Extract user_id from auth_credentials."""
    return auth_credentials["user_id"]

@pytest.fixture
def auth_token(auth_credentials):
    """Extract auth token from auth_credentials."""
    return auth_credentials["token"]

@pytest.fixture
def book_id(api_client):
    """Get a random book ID from the API."""
    from utils.data_factory import get_random_book_id
    response = api_client.books.get_all_books()
    assert response.status_code == 200, "Failed to get books for book_id fixture"
    return get_random_book_id(response)

@pytest.fixture
def cleanup_cart(api_client, user_id, book_id):
    """Clean up cart after test - use only when needed."""
    yield 
    # Cleanup after test
    try:
        api_client.cart.remove_from_cart(user_id, book_id)
    except Exception:
        pass  # Ignore cleanup errors






