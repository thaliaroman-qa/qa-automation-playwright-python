"""Test suite covering the SauceDemo login flow (success and failure cases)."""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
@pytest.mark.login
def test_successful_login_with_standard_user(login_page: LoginPage):
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(login_page.page)
    assert inventory_page.is_loaded()
    assert "inventory.html" in inventory_page.current_url()


@pytest.mark.regression
@pytest.mark.login
def test_login_fails_with_locked_out_user(login_page: LoginPage):
    login_page.login("locked_out_user", "secret_sauce")

    assert login_page.is_error_displayed()
    assert "locked out" in login_page.get_error_message().lower()


@pytest.mark.regression
@pytest.mark.login
def test_login_fails_with_invalid_credentials(login_page: LoginPage):
    login_page.login("invalid_user", "wrong_password")

    assert login_page.is_error_displayed()
    assert "do not match" in login_page.get_error_message().lower()


@pytest.mark.regression
@pytest.mark.login
def test_login_fails_with_empty_credentials(login_page: LoginPage):
    login_page.login("", "")

    assert login_page.is_error_displayed()
    assert "username is required" in login_page.get_error_message().lower()


@pytest.mark.regression
@pytest.mark.login
def test_login_fails_with_missing_password(login_page: LoginPage):
    login_page.login("standard_user", "")

    assert login_page.is_error_displayed()
    assert "password is required" in login_page.get_error_message().lower()
