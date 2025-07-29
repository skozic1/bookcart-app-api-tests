from dataclasses import dataclass, asdict
import random
import string
import json
import requests
from faker import Faker

fake = Faker()

@dataclass
class UserRegistration:
    firstName: str
    lastName: str
    username: str
    password: str
    confirmPassword: str
    gender: str

    def to_dict(self):
        return asdict(self)

def load_test_data(file_path: str = "test_data.json"):
    """Load test data from JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def get_valid_user_credentials():
    """Get first valid user from JSON file."""
    data = load_test_data()
    return random.choice(data["valid_users"])

def get_invalid_user_credentials():
    """Get first invalid user from JSON file."""
    data = load_test_data()
    return random.choice(data["invalid_users"])

def generate_valid_password() -> str:
    """Generate a password that meets requirements: 8+ chars, 1 uppercase, 1 lowercase, 1 number."""
    return fake.password(
        length=8,
        special_chars=False,  
        digits=True,
        upper_case=True,
        lower_case=True
    )

def generate_invalid_password() -> str:
    """Generate invalid password using Faker that doesn't meet requirements."""
    return fake.password(
        length=5,  
        special_chars=False,
        digits=False,  
        upper_case=False,  
        lower_case=True
    )

def generate_valid_registration_data() -> UserRegistration:
    """Generate a valid UserRegistration object with realistic data."""
    password = generate_valid_password()
    return UserRegistration(
        firstName=fake.first_name(),
        lastName=fake.last_name(),
        username=fake.user_name() + str(random.randint(100, 999)),
        password=password,
        confirmPassword=password,
        gender=random.choice(["Male", "Female"])
    )

def generate_invalid_registration_data() -> UserRegistration:
    """Generate invalid UserRegistration object with realistic data but wrong password."""
    return UserRegistration(
        firstName=fake.first_name(),
        lastName=fake.last_name(),
        username=fake.user_name() + str(random.randint(100, 999)),
        password=generate_invalid_password(),
        confirmPassword=generate_invalid_password(),
        gender=random.choice(["Male", "Female"])
    )

def get_random_book_id(response: requests.Response) -> int:
    """Get a random book ID from the API."""
    books = response.json()
    return random.choice(books)["bookId"]

def get_expected_categories():
    """Get expected categories from test data."""
    data = load_test_data()
    return data["expected_categories"]


