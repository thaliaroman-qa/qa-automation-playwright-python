# SauceDemo Test Automation Framework

A professional web test automation project built with **Playwright** and **Python**, using **pytest** as the test runner and the **Page Object Model (POM)** design pattern. The project targets [SauceDemo](https://www.saucedemo.com), a public e-commerce demo site commonly used for QA automation practice.

This repository is intended as a QA Automation portfolio project, showcasing clean test architecture, reusable page objects, and CI/CD integration via GitHub Actions.

## Tech Stack

- **Python 3.11+**
- **Playwright** (sync API) for browser automation
- **pytest** as the test runner
- **pytest-playwright** for Playwright/pytest integration
- **pytest-html** for HTML test reports
- **GitHub Actions** for continuous integration

## Project Structure

```
qa-regresion-portafolio/
├── pages/                     # Page Object Model classes
│   ├── base_page.py           # Shared base page with common helpers
│   ├── login_page.py          # Login page interactions
│   ├── inventory_page.py      # Product listing / cart badge interactions
│   ├── cart_page.py           # Shopping cart interactions
│   └── checkout_page.py       # Checkout flow (info, overview, complete)
├── tests/                     # Test cases
│   ├── test_login.py          # Login: success and failure scenarios
│   ├── test_cart.py           # Add/remove products from the cart
│   └── test_checkout.py       # End-to-end checkout flow
├── conftest.py                # Shared pytest fixtures (browser, page, login)
├── pytest.ini                 # pytest configuration and markers
├── requirements.txt           # Python dependencies
└── .github/workflows/tests.yml # CI/CD pipeline (GitHub Actions)
```

## Page Object Model

Each page of the application is represented as a class encapsulating its locators and interactions:

- `LoginPage` — fill credentials, submit login, read error messages
- `InventoryPage` — add/remove products, read cart badge count, sort products, navigate to cart
- `CartPage` — read cart contents, remove products, proceed to checkout
- `CheckoutPage` — fill shipping information, read order summary, finish the order

Tests only interact with these page classes — never with raw selectors — keeping tests readable and resilient to UI changes.

## Test Coverage

| File | Scenarios |
|---|---|
| `test_login.py` | Successful login, locked-out user, invalid credentials, empty username, empty password |
| `test_cart.py` | Add a single product, add multiple products, remove from inventory page, remove from cart page, verify cart contents |
| `test_checkout.py` | Full checkout flow (add → cart → checkout → confirmation), checkout validation error, order summary total |

Markers are available to run subsets of the suite: `smoke`, `regression`, `login`, `cart`, `checkout`.

## Getting Started

### Prerequisites

- Python 3.11 or newer
- pip

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd qa-regresion-portafolio

# (Recommended) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Install Playwright browser binaries
playwright install
```

### Running the tests

```bash
# Run the full suite
pytest

# Run a specific file
pytest tests/test_login.py

# Run tests by marker
pytest -m smoke
pytest -m "login or cart"

# Run with visible browser (headed mode)
pytest --headed

# Run in a specific browser
pytest --browser firefox
```

An HTML report (`report.html`) is generated automatically after each run, thanks to the `pytest-html` configuration in `pytest.ini`.

### Test users

SauceDemo provides several test accounts (password for all: `secret_sauce`):

| Username | Behavior |
|---|---|
| `standard_user` | Normal user, full access |
| `locked_out_user` | Login is blocked with an error message |
| `problem_user` | Login succeeds but the UI has known bugs |
| `performance_glitch_user` | Login succeeds with artificial delay |

## Continuous Integration

The GitHub Actions workflow at `.github/workflows/tests.yml` runs the full test suite automatically on every push and pull request to `main`/`master`, and can also be triggered manually. It:

1. Checks out the repository
2. Sets up Python
3. Installs project dependencies
4. Installs Playwright's Chromium browser
5. Runs the pytest suite
6. Uploads the generated HTML report as a build artifact

## Design Notes

- Fixtures in `conftest.py` manage the Playwright lifecycle (`browser` → `context` → `page`) so each test runs in an isolated browser context.
- A `logged_in_page` fixture centralizes the login step for tests that don't need to verify login behavior itself.
- Page objects avoid exposing raw Playwright locators to tests; each page method returns plain data (strings, counts, booleans) that tests can assert on directly.
