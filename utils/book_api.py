import requests
from utils.base_api import BaseAPI

class BookAPI(BaseAPI):
    """API methods for book browsing and search."""
    
    def get_all_books(self) -> requests.Response:
        """Get all books from the API."""
        return requests.get(f"{self.base_url}/Book")

    def get_book_by_id(self, book_id: int) -> requests.Response:
        """Get a book by ID."""
        return requests.get(f"{self.base_url}/Book/{book_id}")

    def get_similar_books(self, book_id: int) -> requests.Response:
        """Get similar books for a specific book."""
        return requests.get(f"{self.base_url}/Book/GetSimilarBooks/{book_id}")

    def get_categories(self) -> requests.Response:
        """Get all book categories."""
        return requests.get(f"{self.base_url}/Book/GetCategoriesList") 