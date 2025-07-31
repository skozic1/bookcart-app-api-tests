# Book Cart API – Test Plan

**Author:** Sara Kozic Bubalo  
**Date:** July 2025  
**Repository:** [bookcart-app-api-tests](https://github.com/skozic1/bookcart-app-api-tests)  
**Application:** [Book Cart](https://bookcart.azurewebsites.net/)  
**API Documentation:** [Swagger UI](https://bookcart.azurewebsites.net/swagger/index.html)

---

## 1. Executive Summary

This test plan outlines the API testing approach for the Book Cart application, focusing on the key functionalities requested in the assignment. The testing strategy covers functional API testing with real user flows, automated using Python and pytest.

### 1.1 Testing Objectives
- **Functional Validation:** Ensure core API endpoints work as expected
- **Business Logic Verification:** Validate critical user workflows
- **Data Integrity:** Verify data consistency across operations
- **Error Handling:** Test edge cases and failure scenarios
- **Automation:** Create maintainable automated test suite

### 1.2 Success Criteria
- Core API endpoints covered with automated tests
- Critical user flows functional and tested
- Comprehensive error handling for main scenarios
- Automated test suite with high pass rate
- Clean, maintainable code following best practices

---

## 2. Application Analysis & Scope

### 2.1 Application Overview
- **Type:** E-commerce book store application
- **API Style:** RESTful with JSON request/response
- **Key Features:** User registration, book browsing, shopping cart, order management



### 2.2 Testing Scope
-  **API Testing** - Core business functionality
-  **User Flow Testing** - End-to-end workflows
-  **Data Validation** - Request/response validation
-  **Error Handling** - Negative test scenarios

---

## 3. Test Strategy & Framework

### 3.1 Technology Stack
- **Language:** Python 3.12.1
- **Framework:** pytest 8.4.1
- **HTTP Client:** requests library
- **Test Data:** Faker library
- **Reporting:** pytest-html
- **Configuration:** pytest.ini

### 3.2 Design Patterns Implemented
- **Page Object Model (POM)** - API client abstraction
- **Factory Pattern** - Test data generation
- **Modular Design** - Separated concerns and responsibilities

### 3.3 Test Data Strategy
- **Dynamic Generation:** Faker for realistic data
- **Static Data:** Pre-defined test users in test_data.json
- **Data Isolation:** Each test uses unique data where needed

### 3.4 Risk Assessment

| Risk | Impact | Probability | Mitigation Strategy |
|------|--------|-------------|-------------------|
| **API Changes** | High | Medium | Monitor Swagger documentation regularly, maintain flexible test framework |
| **Environment Issues** | High | Low | Use stable Azure environment, maintain backup test data |
| **Time Constraints** | Medium | Medium | Prioritize smoke tests, focus on critical user flows |
| **Data Dependencies** | Medium | Low | Use dynamic data generation, minimize external dependencies |
| **Framework Maintenance** | Low | Low | Clean code practices, modular architecture |

---

## 4. Test Scenarios
### 4.1 Test Scenarios

#### **4.1.1 Smoke Test Suite (Critical Path)**

| Test Case | Purpose | Business Impact |
|-----------|---------|-----------------|
| `test_registration_smoke` | User account creation | User acquisition |
| `test_login_smoke` | User authentication | User access |
| `test_book_categories_smoke` | Book categories validation | Core functionality |
| `test_shopping_cart_smoke` | Basic cart operations | Revenue generation |
| `test_book_browsing_smoke` | Book discovery flow | User experience |
| `test_order_checkout_smoke` | Complete purchase flow | Business completion |

#### **4.1.2 Positive Test Scenarios**

**User Management**
- Valid user registration with all required fields (POST /api/User)
- User login with correct credentials (POST /api/Login)
- Username validation (GET /api/User/validateUserName/{userName})
-  User profile retrieval (GET /api/User/{userId})

**Book Catalog**
- Retrieve complete book catalog (GET /api/Book)
- Get book details by ID (GET /api/Book/{id})
- Get similar book recommendations (GET /api/Book/GetSimilarBooks/{bookId})
- Category listing and validation (GET /api/Book/GetCategoriesList)

**Shopping Cart**
- Add book to cart (POST /api/ShoppingCart/AddToCart/{userId}/{bookId})
- View cart contents (GET /api/ShoppingCart/{userId})
- Remove book from cart (DELETE /api/ShoppingCart/{userId}/{bookId})

**Order Management**
- Complete checkout process (POST /api/CheckOut/{userId})
- Order history retrieval (GET /api/Order/{userId})

**End-to-End (E2E) User Flows**
*End-to-End tests simulate real user journeys through the entire application, testing integration between different API endpoints and business flows.*

- **Book Discovery Flow (Smoke):** Get All Books → Get Book Details → Get Similar Books
- **Complete Purchase Flow (Smoke):** Add to Cart → Verify Cart → Checkout → Verify Order History
- **Shopping Cart Management Flow:** Add Books → Update Quantities → Remove Items → Transfer Cart → Checkout
- **Order Processing Flow:** Browse Categories → Filter Books → Get Book Details → Find Similar Books → Add to Cart
- **Guest User Flow:** Browse Books → Add to Cart → Register → Complete Purchase → Verify Order
- **Bulk Purchase Flow:** Browse Multiple Categories → Add Many Books → Review Large Cart → Checkout → Verify Order
- **User Session Flow:** Login → Browse → Add Items → Logout → Login Again → Verify Cart Persistence
- **Error Recovery Flow:** Failed Login → Retry → Success → Continue Shopping → Complete Purchase

#### **4.1.3 Negative Test Scenarios**

**Login Validation**
-  Login with invalid credentials (POST /api/Login)
-  Registration with invalid password format (POST /api/User)
-  Login with non-existent username (POST /api/Login)
-  Registration with duplicate username (POST /api/User)
-  Login with empty credentials (POST /api/Login)
-  Login with empty username (POST /api/Login)
-  Login with empty password (POST /api/Login)

**Data Validation**
-  Invalid book ID requests (non-existent book) (GET /api/Book/{id})
-  Negative book ID requests (GET /api/Book/{id})
-  Empty cart operations (GET /api/ShoppingCart/{userId})
-  Add non-existent book to cart (POST /api/ShoppingCart/AddToCart/{userId}/{bookId})
-  Remove book from empty cart (DELETE /api/ShoppingCart/{userId}/{bookId})
-  Checkout with empty cart (POST /api/CheckOut/{userId})

**Input Validation**
-  Registration with missing required fields (POST /api/User)
-  Registration with invalid email format (POST /api/User)
-  Registration with too short password (POST /api/User)

**Business Logic**
-  Checkout without being logged in (POST /api/CheckOut/{userId})
-  Checkout with invalid authentication token (POST /api/CheckOut/{userId})
-  Access order history for non-existent user (GET /api/Order/{userId})
-  Get order history with invalid token (GET /api/Order/{userId})
-  Add book to cart for non-existent user (POST /api/ShoppingCart/AddToCart/{userId}/{bookId})
-  Get cart for non-existent user (GET /api/ShoppingCart/{userId})
-  Add book with negative user ID (POST /api/ShoppingCart/AddToCart/{userId}/{bookId})
-  Add book with negative book ID (POST /api/ShoppingCart/AddToCart/{userId}/{bookId})

---

## 5. Bug Analysis & Quality Metrics

### 5.1 Quality Metrics
- **API Endpoints Coverage:** 59% coverage (13/22 endpoints tested)
- **Total Test Cases:** 10 automated + 38 available = 48 total
- **Test Execution Time:** ~4-5 seconds per test
- **Automation Rate:** 21% (10/48 total test cases are automated)

#### **5.1.1 Detailed Endpoints Coverage**

| Domain | Endpoints Tested | HTTP Methods | Coverage |
|--------|------------------|--------------|----------|
| **User Management** | `/api/User`, `/api/Login`, `/api/User/validateUserName/{userName}` | POST, GET | 75% (3/4 endpoints) |
| **Book Catalog** | `/api/Book`, `/api/Book/{id}`, `/api/Book/GetCategoriesList`, `/api/Book/GetSimilarBooks/{bookId}` | GET | 57% (4/7 endpoints) |
| **Shopping Cart** | `/api/ShoppingCart/{userId}`, `/api/ShoppingCart/AddToCart/{userId}/{bookId}`, `/api/ShoppingCart/{userId}/{bookId}` | GET, POST, DELETE | 50% (3/6 endpoints) |
| **Orders** | `/api/Order/{userId}`, `/api/CheckOut/{userId}` | GET, POST | 100% (2/2 endpoints) |
| **Wishlist** | - | - | 0% (0/3 endpoints) |

### 5.2 Bug Reporting Process

**For detailed bug reports with steps to reproduce, see [BUGS.md](BUGS.md).**


---

## 6. Automation Framework Architecture

### 6.1 Project Structure
```
bookcart-api-tests/
├── tests/                     # Test implementations
│   ├── test_registration.py   # User registration tests
│   ├── test_login.py         # Authentication tests
│   ├── test_book_browsing.py # Catalog tests
│   ├── test_shopping_cart.py # Cart operations
│   └── test_orders.py        # Order management
├── utils/                     # Framework utilities
│   ├── api_client.py         # Main API client
│   ├── user_api.py           # User domain API
│   ├── book_api.py           # Book domain API
│   ├── cart_api.py           # Cart domain API
│   └── data_factory.py       # Test data generation
├── screenshots/               
│   ├── swagger_registration_test.png
│   ├── wrongPassword-login.gif
│   └── registration-gender-bug.gif
├── test_data.json            # Static test data
├── requirements.txt          # Python dependencies
├── pytest.ini               # Pytest configuration
├── README.md                # Setup and execution guide
├── BUGS.md                  # Bug documentation
└── TEST_PLAN.md             # This document
```


## 7. Test Execution

**For detailed setup instructions and test execution commands,  refer to [README.md](README.md).**

**Quick Start:**
```bash
# Clone, setup environment, and run smoke tests
git clone https://github.com/skozic1/bookcart-app-api-tests.git
cd bookcart-app-api-tests
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
pytest -m smoke
```

---

