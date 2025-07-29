import pytest

@pytest.mark.smoke
def test_order_checkout_smoke(api_client, user_id, auth_token, book_id, logger, cleanup_cart):
    """Smoke test: Complete order checkout flow."""
    logger.info(f"Starting order checkout test with book ID: {book_id}")
    
    # Add book to cart
    response = api_client.cart.add_to_cart(user_id, book_id)
    assert response.status_code == 200, f"Failed to add book to cart! Expected 200, got {response.status_code}"
    
    # Verify book was added to cart
    response = api_client.cart.get_cart_items(user_id)
    assert response.status_code == 200, f"Failed to get cart items! Expected 200, got {response.status_code}"
    
    cart_items = response.json()
    assert len(cart_items) > 0, "Cart is empty after adding book"
    logger.info(f"Cart contains {len(cart_items)} items")
    
    # Verify our book is in the cart
    book_found = False
    for item in cart_items:
        if item.get('book', {}).get('bookId') == book_id:
            book_found = True
            logger.info(f"Found our book {book_id} in cart")
            break
    
    assert book_found, f"Book {book_id} not found in cart after adding"
    
    # Prepare order data
    order_data = {
        "orderDetails": cart_items,
        "cartTotal": len(cart_items)
    }
    
    # Complete checkout
    response = api_client.cart.checkout(user_id=user_id, order_data=order_data, token=auth_token)
    assert response.status_code == 200, f"Failed to checkout! Expected 200, got {response.status_code}"
    logger.info("Checkout completed successfully")
    
    # Verify order appears in history
    response = api_client.cart.get_order_history(user_id, auth_token)
    assert response.status_code == 200, f"Failed to get order history! Expected 200, got {response.status_code}"
    
    order_history = response.json()
    logger.info(f"Found {len(order_history)} orders in history")
    
    # Find our order in history
    our_order = None
    for order in order_history:
        for item in order.get('orderDetails', []):
            if item.get('book', {}).get('bookId') == book_id:
                our_order = order
                logger.info(f"Found our order in history with order ID: {order.get('orderId', 'N/A')}")
                break
        if our_order:
            break
    
    assert our_order is not None, f"Order with book {book_id} not found in order history"
    
    # Verify order has required fields
    assert 'orderId' in our_order, "Order missing orderId field"
    assert 'orderDetails' in our_order, "Order missing orderDetails field"
    assert len(our_order['orderDetails']) > 0, "Order has no items"
    
    logger.info("Order checkout test completed successfully!")

    