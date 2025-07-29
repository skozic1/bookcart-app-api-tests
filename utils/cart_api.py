import requests
from utils.base_api import BaseAPI

class CartAPI(BaseAPI):
    """API methods for shopping cart operations."""
    
    def add_to_cart(self, user_id: int, book_id: int) -> requests.Response:
        """Add a book to the shopping cart."""
        return requests.post(f"{self.base_url}/ShoppingCart/AddToCart/{user_id}/{book_id}")
        
    def get_cart_items(self, user_id: int) -> requests.Response:
        """Get all items in the shopping cart."""
        return requests.get(f"{self.base_url}/ShoppingCart/{user_id}")

    def remove_from_cart(self, user_id: int, book_id: int) -> requests.Response:
        """Remove a book from the shopping cart."""
        return requests.delete(f"{self.base_url}/ShoppingCart/{user_id}/{book_id}")
    
    def checkout(self, user_id: int, order_data: dict, token: str = None) -> requests.Response:
        """Checkout cart and create order."""
        headers = {'Content-Type': 'application/json'}
        if token:
            headers['Authorization'] = f'Bearer {token}'
        return requests.post(f"{self.base_url}/CheckOut/{user_id}", json=order_data, headers=headers)
    
    def get_order_history(self, user_id: int, token: str = None) -> requests.Response:
        """Get order history for a user."""
        headers = {}
        if token:
            headers['Authorization'] = f'Bearer {token}'
        return requests.get(f"{self.base_url}/Order/{user_id}", headers=headers) 