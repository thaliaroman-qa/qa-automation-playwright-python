"""Test suite covering adding and removing products from the SauceDemo cart."""
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.smoke
@pytest.mark.cart
def test_add_single_product_to_cart(logged_in_page: InventoryPage):
    logged_in_page.add_product_to_cart("Sauce Labs Backpack")

    assert logged_in_page.get_cart_badge_count() == "1"


@pytest.mark.regression
@pytest.mark.cart
def test_add_multiple_products_to_cart(logged_in_page: InventoryPage):
    logged_in_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_page.add_product_to_cart("Sauce Labs Bike Light")
    logged_in_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")

    assert logged_in_page.get_cart_badge_count() == "3"


@pytest.mark.regression
@pytest.mark.cart
def test_remove_product_from_inventory_page(logged_in_page: InventoryPage):
    logged_in_page.add_product_to_cart("Sauce Labs Backpack")
    assert logged_in_page.get_cart_badge_count() == "1"

    logged_in_page.remove_product_from_cart("Sauce Labs Backpack")
    assert logged_in_page.get_cart_badge_count() == "0"


@pytest.mark.regression
@pytest.mark.cart
def test_remove_product_from_cart_page(logged_in_page: InventoryPage):
    logged_in_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_page.add_product_to_cart("Sauce Labs Bike Light")
    logged_in_page.go_to_cart()

    cart_page = CartPage(logged_in_page.page)
    assert cart_page.get_cart_items_count() == 2

    cart_page.remove_product("Sauce Labs Backpack")
    assert cart_page.get_cart_items_count() == 1
    assert "Sauce Labs Backpack" not in cart_page.get_cart_items()


@pytest.mark.smoke
@pytest.mark.cart
def test_cart_contents_match_selected_products(logged_in_page: InventoryPage):
    logged_in_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_page.add_product_to_cart("Sauce Labs Onesie")
    logged_in_page.go_to_cart()

    cart_page = CartPage(logged_in_page.page)
    items = cart_page.get_cart_items()

    assert "Sauce Labs Backpack" in items
    assert "Sauce Labs Onesie" in items
    assert len(items) == 2
