"""Test suite covering the SauceDemo checkout flow."""
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
@pytest.mark.checkout
def test_complete_checkout_flow_successfully(logged_in_page: InventoryPage):
    logged_in_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_page.add_product_to_cart("Sauce Labs Bike Light")
    logged_in_page.go_to_cart()

    cart_page = CartPage(logged_in_page.page)
    cart_page.checkout()

    checkout_page = CheckoutPage(logged_in_page.page)
    checkout_page.fill_information("Thalia", "Roman", "12345")

    assert "total" in checkout_page.get_total_summary().lower()

    checkout_page.finish_checkout()

    assert checkout_page.is_order_complete()
    assert "thank you for your order" in checkout_page.get_complete_header().lower()


@pytest.mark.regression
@pytest.mark.checkout
def test_checkout_fails_with_missing_information(logged_in_page: InventoryPage):
    logged_in_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_page.go_to_cart()

    cart_page = CartPage(logged_in_page.page)
    cart_page.checkout()

    checkout_page = CheckoutPage(logged_in_page.page)
    checkout_page.fill_information("", "", "")

    assert "first name is required" in checkout_page.get_error_message().lower()


@pytest.mark.regression
@pytest.mark.checkout
def test_checkout_step_two_shows_correct_item_total(logged_in_page: InventoryPage):
    logged_in_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_page.go_to_cart()

    cart_page = CartPage(logged_in_page.page)
    cart_page.checkout()

    checkout_page = CheckoutPage(logged_in_page.page)
    checkout_page.fill_information("Thalia", "Roman", "12345")

    assert "$" in checkout_page.get_total_summary()
