# Book Cart API Tests

Automated API testing framework for the Book Cart application using Python and pytest.

## Prerequisites
- Python 3.9 or higher (tested with Python 3.12.1)
- pip (Python package installer)

## Dependencies
- **pytest** - Testing framework
- **requests** - HTTP client for API calls
- **pytest-html** - HTML test reports
- **Faker** - Realistic test data generation

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/skozic1/bookcart-api-tests.git
   cd bookcart-api-tests
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

### Basic Commands
```bash
# Run all tests
pytest

# Run only smoke tests
pytest -m smoke

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_orders.py

# Run specific test function
pytest tests/test_orders.py::test_order_checkout_smoke
```

### Generate HTML Report
```bash
# HTML report
pytest --html=test-report.html --self-contained-html

# Open HTML report in browser
start test-report.html
```

## Test Structure

### Test Files
- `tests/test_orders.py` - Order checkout flow
- `tests/test_shopping_cart.py` - Shopping cart operations  
- `tests/test_book_browsing.py` - Book browsing and categories
- `tests/test_login.py` - User authentication
- `tests/test_registration.py` - User registration

### Test Categories
- **Smoke Tests** (`@pytest.mark.smoke`) - Critical user flows
- **Regression Tests** - Comprehensive testing

### Test Data
- `test_data.json` - Test users and expected data
- `utils/data_factory.py` - Dynamic test data generation using Faker

## Project Structure
```
bookcart-api-tests/
├── .github/workflows/     # CI/CD workflows
├── tests/                 # Test files
├── utils/                 # Utility modules
├── test_data.json        # Test data
├── requirements.txt      # Python dependencies
└── README.md            # This file
```



