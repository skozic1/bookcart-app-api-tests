import pytest
from utils.data_factory import get_random_book_id, get_expected_categories

@pytest.mark.smoke
def test_book_browsing_smoke(api_client, logger):
    """Smoke test: Browse books and get similar books."""
    logger.info("Starting Book Browsing Smoke Test")
    
    # Get all books
    response = api_client.books.get_all_books()
    assert response.status_code == 200, f"Failed to get books! Expected 200, got {response.status_code}"
    
    books = response.json()
    logger.info(f"Found {len(books)} books in the catalog")
    assert len(books) > 0, "No books found in the catalog"

    # Get a random book ID
    book_id = get_random_book_id(response)
    logger.info(f"Selected book ID: {book_id}")

    # Get book details by ID
    response = api_client.books.get_book_by_id(book_id)
    assert response.status_code == 200, f"Failed to get book by ID! Expected 200, got {response.status_code}"
    
    book_data = response.json()
    logger.info(f"Book details: '{book_data['title']}' by {book_data['author']}")
    
    # Verify book has all required fields
    required_fields = ["bookId", "title", "author", "category", "price"]
    for field in required_fields:
        assert field in book_data, f"Book is missing required field: {field}"
    
    # Verify book ID matches
    assert book_data["bookId"] == book_id, f"Book ID mismatch: expected {book_id}, got {book_data['bookId']}"
    
    # Verify basic data validity
    assert book_data["title"], f"Book title cannot be empty"
    assert book_data["author"], f"Book author cannot be empty"
    assert book_data["price"] >= 0, f"Book price should be non-negative, got {book_data['price']}"
    
    book_category = book_data["category"]
    logger.info(f"Book category: {book_category}")

    # Get similar books
    logger.info(f"Getting similar books for book {book_id}")
    response = api_client.books.get_similar_books(book_id)
    assert response.status_code == 200, f"Failed to get similar books! Expected 200, got {response.status_code}"
    
    similar_books = response.json()
    logger.info(f"Found {len(similar_books)} similar books")
    
    # Verify similar books have matching category
    if similar_books:
        for book in similar_books:
            assert book["category"] == book_category, \
                f"Similar book has wrong category! Expected: {book_category}, got: {book['category']}"
        logger.info("All similar books have matching category")
    else:
        logger.info("No similar books found (this is OK)")
    
    logger.info("Book Browsing Smoke Test completed successfully!")

@pytest.mark.smoke
def test_book_categories_smoke(api_client, logger):
    """Smoke test: Validate book categories against expected data."""
    
    logger.info("Starting Book Categories Validation Test")
    
    # Get categories from API
    response = api_client.books.get_categories()
    assert response.status_code == 200, f"Failed to get categories! Expected 200, got {response.status_code}"
    
    actual_categories = response.json()
    expected_categories = get_expected_categories()
    
    logger.info(f"Found {len(actual_categories)} categories in API")
    logger.info(f"Expected {len(expected_categories)} categories from test data")
    
    # Verify we have at least the expected number of categories
    assert len(actual_categories) >= len(expected_categories), \
        f"API returned fewer categories than expected. Expected at least {len(expected_categories)}, got {len(actual_categories)}"
    
    # Verify each expected category exists
    for expected_category in expected_categories:
        category_found = False
        for actual_category in actual_categories:
            if (actual_category.get("categoryId") == expected_category["categoryId"] and 
                actual_category.get("categoryName") == expected_category["categoryName"]):
                category_found = True
                logger.info(f"Found expected category: {expected_category['categoryName']} (ID: {expected_category['categoryId']})")
                break
        
        if not category_found:
            logger.error(f"Missing expected category: {expected_category['categoryName']} (ID: {expected_category['categoryId']})")
            assert False, f"Expected category not found: {expected_category['categoryName']} (ID: {expected_category['categoryId']})"
    
    logger.info("All expected categories found in API response!")
    logger.info("Book Categories Validation Test completed successfully")
