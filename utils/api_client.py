from utils.user_api import UserAPI
from utils.book_api import BookAPI
from utils.cart_api import CartAPI

class BookCartClient:
    """Main client that provides access to all API categories."""
    
    def __init__(self, base_url: str):
        self.users = UserAPI(base_url)
        self.books = BookAPI(base_url)
        self.cart = CartAPI(base_url)