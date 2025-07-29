import requests
from utils.data_factory import UserRegistration
from utils.base_api import BaseAPI

class UserAPI(BaseAPI):
    """API methods for user management (registration, login)."""
    
    def register_user(self, user: UserRegistration) -> requests.Response:
        """Register a new user."""
        return requests.post(f"{self.base_url}/User", json=user.to_dict())

    def validate_username(self, username: str) -> bool:
        """Validate username."""
        url = f"{self.base_url}/User/validateUserName/{username}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json() is True

    def login_user(self, username: str, password: str) -> requests.Response:
        """Login and return response"""
        payload = {
            "username": username,
            "password": password
        }
        return requests.post(f"{self.base_url}/login", json=payload) 