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
- **API Object Model** - API client abstraction
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

#### **4.1.1 Positive Test Scenarios**

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

| Test Case | Steps | Endpoints Used |
|-----------|-------|----------------|
| **E2E_Complete_Purchase_Flow** | 1. Login user<br>2. Add book to cart<br>3. Get cart contents<br>4. Complete checkout<br>5. Verify order history | POST /api/Login<br>POST /api/ShoppingCart/AddToCart/{userId}/{bookId}<br>GET /api/ShoppingCart/{userId}<br>POST /api/CheckOut/{userId}<br>GET /api/Order/{userId} |
| **E2E_User_Registration_Flow** | 1. Validate username availability<br>2. Register new user<br>3. Login with new credentials | GET /api/User/validateUserName/{userName}<br>POST /api/User<br>POST /api/Login |
| **E2E_Shopping_Cart_Management** | 1. Login user<br>2. Add book to cart<br>3. Get cart contents<br>4. Remove book from cart<br>5. Verify empty cart | POST /api/Login<br>POST /api/ShoppingCart/AddToCart/{userId}/{bookId}<br>GET /api/ShoppingCart/{userId}<br>DELETE /api/ShoppingCart/{userId}/{bookId}<br>GET /api/ShoppingCart/{userId} |
| **E2E_Category_Browsing_Flow** | 1. Get all categories<br>2. Get all books<br>3. Get book details<br>4. Get similar books | GET /api/Book/GetCategoriesList<br>GET /api/Book<br>GET /api/Book/{id}<br>GET /api/Book/GetSimilarBooks/{bookId} |
| **E2E_Multi_Book_Purchase** | 1. Login user<br>2. Add first book to cart<br>3. Add second book to cart<br>4. Get cart contents<br>5. Complete checkout<br>6. Verify order history | POST /api/Login<br>POST /api/ShoppingCart/AddToCart/{userId}/{bookId1}<br>POST /api/ShoppingCart/AddToCart/{userId}/{bookId2}<br>GET /api/ShoppingCart/{userId}<br>POST /api/CheckOut/{userId}<br>GET /api/Order/{userId} |
| **E2E_Book_Recommendation_Flow** | 1. Get all books<br>2. Select random book<br>3. Get book details<br>4. Get similar books<br>5. Get details of similar book | GET /api/Book<br>GET /api/Book/{id}<br>GET /api/Book/GetSimilarBooks/{bookId}<br>GET /api/Book/{similarBookId} |
| **E2E_Order_History_Flow** | 1. Login user<br>2. Complete purchase<br>3. Get order history<br>4. Verify order details | POST /api/Login<br>POST /api/CheckOut/{userId}<br>GET /api/Order/{userId} |
| **E2E_User_Profile_Flow** | 1. Register new user<br>2. Login user<br>3. Validate username<br>4. Get user profile | POST /api/User<br>POST /api/Login<br>GET /api/User/validateUserName/{userName} |

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

#### **4.1.4 Smoke Test Suite (Critical Path)**

| Test Case | Steps | Endpoints Tested |
|-----------|-------|------------------|
| `test_registration_smoke` | 1. Generate valid user data<br>2. Register new user | POST /api/User |
| `test_login_smoke` | 1. Get valid user credentials<br>2. Login user<br>3. Verify response structure | POST /api/Login |
| `test_book_categories_smoke` | 1. Get all book categories<br>2. Verify categories list | GET /api/Book/GetCategoriesList |
| `test_shopping_cart_smoke` | 1. Add book to cart<br>2. Get cart contents<br>3. Verify book is in cart | POST /api/ShoppingCart/AddToCart/{userId}/{bookId}<br>GET /api/ShoppingCart/{userId} |
| `test_book_by_id_smoke` | 1. Get all books<br>2. Get book details by random ID | GET /api/Book<br>GET /api/Book/{id} |
| `test_order_checkout_smoke` | 1. Add book to cart<br>2. Get cart contents<br>3. Complete checkout<br>4. Verify order history | POST /api/ShoppingCart/AddToCart/{userId}/{bookId}<br>GET /api/ShoppingCart/{userId}<br>POST /api/CheckOut/{userId}<br>GET /api/Order/{userId} |

---

## 5. Bug Analysis & Quality Metrics

### 5.1 Quality Metrics
- **API Endpoints Coverage:** 59% coverage (13/22 endpoints tested)
- **Total Test Cases:** 11 automated + 38 available = 49 total
- **Test Execution Time:** ~4-5 seconds per test
- **Automation Rate:** 22% (11/49 total test cases are automated)

#### **5.1.1 Detailed Endpoints Coverage**

| Domain | Endpoints Tested | HTTP Methods | Coverage |
|--------|------------------|--------------|----------|
| **User Management** | `/api/User`, `/api/Login`, `/api/User/validateUserName/{userName}` | POST, GET | 75% (3/4 endpoints) |
| **Book Catalog** | `/api/Book`, `/api/Book/{id}`, `/api/Book/GetCategoriesList`, `/api/Book/GetSimilarBooks/{bookId}` | GET | 57% (4/7 endpoints) |
| **Shopping Cart** | `/api/ShoppingCart/{userId}`, `/api/ShoppingCart/AddToCart/{userId}/{bookId}`, `/api/ShoppingCart/{userId}/{bookId}` | GET, POST, DELETE | 50% (3/6 endpoints) |
| **Orders** | `/api/Order/{userId}`, `/api/CheckOut/{userId}` | GET, POST | 100% (2/2 endpoints) |
| **Wishlist** | - | - | 0% (0/3 endpoints) |

#### **5.1.2 Automated Test Coverage**

| Test File | Test Function | Category |
|-----------|---------------|----------|
| `test_registration.py` | `test_registration_smoke` | Smoke |
| `test_registration.py` | `test_registration_functional` | Functional |
| `test_registration.py` | `test_registration_negative` | Negative |
| `test_login.py` | `test_login_smoke` | Smoke |
| `test_login.py` | `test_login_negative` | Negative |
| `test_book_browsing.py` | `test_book_by_id_smoke` | Smoke |
| `test_book_browsing.py` | `test_book_categories_smoke` | Smoke |
| `test_book_browsing.py` | `test_book_browsing_functional` | Functional |
| `test_shopping_cart.py` | `test_shopping_cart_smoke` | Smoke |
| `test_shopping_cart.py` | `test_shopping_cart_functional` | Functional |
| `test_orders.py` | `test_order_checkout_smoke` | Smoke |

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

