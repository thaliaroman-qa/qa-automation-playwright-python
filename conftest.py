"""Shared pytest fixtures for the SauceDemo test suite."""
import pytest
from playwright.sync_api import sync_playwright, Browser, Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

BASE_URL = "https://www.saucedemo.com/"
STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
VALID_PASSWORD = "secret_sauce"


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture
def context(browser: Browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context) -> Page:
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login_page = LoginPage(page)
    login_page.navigate()
    return login_page


@pytest.fixture
def logged_in_page(page: Page) -> InventoryPage:
    """Logs in with a standard user and returns the loaded InventoryPage."""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(STANDARD_USER, VALID_PASSWORD)
    return InventoryPage(page)
