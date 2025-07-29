class BaseAPI:
    """Base class for all API clients with common initialization."""
    
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/') 