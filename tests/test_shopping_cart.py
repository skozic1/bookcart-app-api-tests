import pytest

@pytest.mark.smoke
def test_shopping_cart_smoke(api_client, user_id, book_id, logger):
    """Smoke test: Add a book to the cart and verify it's there."""
    logger.info("Starting Shopping Cart Smoke Test")

    # Add book to cart
    logger.info(f"Adding book {book_id} to cart")
    response = api_client.cart.add_to_cart(user_id, book_id) 
    assert response.status_code == 200, f"Failed to add book to cart! Expected 200, got {response.status_code}"
    
    # Verify book was added to cart
    response = api_client.cart.get_cart_items(user_id)
    assert response.status_code == 200, f"Failed to get cart items! Expected 200, got {response.status_code}"
    
    cart_items = response.json()
    logger.info(f"Cart contains {len(cart_items)} items")
    
    # Verify our book is in the cart
    book_found = False
    for item in cart_items:
        if item.get('book', {}).get('bookId') == book_id:
            book_found = True
            logger.info(f"Found our book {book_id} in cart!")
            break
    
    assert book_found, f"Book {book_id} not found in cart after adding"
    
    logger.info("Shopping Cart Smoke Test completed successfully!")

@pytest.mark.functional
def test_shopping_cart_functional(api_client, user_id, book_id, logger):
    """Functional test: Complete shopping cart flow - add, verify, remove, verify."""
    logger.info("Starting Shopping Cart Complete Flow Test")

    # Add book to cart
    logger.info(f"Adding book {book_id} to cart")
    response = api_client.cart.add_to_cart(user_id, book_id) 
    assert response.status_code == 200, f"Failed to add book to cart! Expected 200, got {response.status_code}"
    
    # Verify book was added to cart
    response = api_client.cart.get_cart_items(user_id)
    assert response.status_code == 200, f"Failed to get cart items! Expected 200, got {response.status_code}"
    
    cart_items = response.json()
    logger.info(f"Cart contains {len(cart_items)} items")
    
    # Verify our book is in the cart
    book_found = False
    for item in cart_items:
        if item.get('book', {}).get('bookId') == book_id:
            book_found = True
            logger.info(f"Found our book {book_id} in cart!")
            break
    
    assert book_found, f"Book {book_id} not found in cart after adding"

    # Remove book from cart
    logger.info(f"Removing book {book_id} from cart")
    response = api_client.cart.remove_from_cart(user_id, book_id)
    assert response.status_code == 200, f"Failed to remove book from cart! Expected 200, got {response.status_code}"
    
    # Verify book was removed from cart
    response = api_client.cart.get_cart_items(user_id)
    assert response.status_code == 200, f"Failed to get cart items after removal! Expected 200, got {response.status_code}"
    
    cart_items_after_removal = response.json()
    
    if len(cart_items_after_removal) == 0:
        logger.info("Cart is empty after removal")
    else:
        # Verify our book is not in the cart anymore
        for item in cart_items_after_removal:
            assert item.get('book', {}).get('bookId') != book_id, f"Book {book_id} is still in the cart after removal"
        logger.info(f"Cart contains {len(cart_items_after_removal)} other items")

    logger.info("Shopping Cart Complete Flow Test completed successfully!")