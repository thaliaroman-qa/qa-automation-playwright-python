"""Page Object for the SauceDemo inventory (products) page."""
from playwright.sync_api import Page
from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    PAGE_TITLE = ".title"
    INVENTORY_ITEM = ".inventory_item"
    ITEM_NAME = ".inventory_item_name"
    CART_ICON = ".shopping_cart_link"
    CART_BADGE = ".shopping_cart_badge"
    SORT_DROPDOWN = ".product_sort_container"
    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def __init__(self, page: Page):
        super().__init__(page)

    def _add_to_cart_button(self, product_name: str):
        slug = product_name.lower().replace(" ", "-").replace("(", "").replace(")", "")
        return f"[data-test='add-to-cart-{slug}']"

    def _remove_button(self, product_name: str):
        slug = product_name.lower().replace(" ", "-").replace("(", "").replace(")", "")
        return f"[data-test='remove-{slug}']"

    def is_loaded(self) -> bool:
        return self.page.locator(self.PAGE_TITLE).inner_text() == "Products"

    def add_product_to_cart(self, product_name: str):
        self.page.click(self._add_to_cart_button(product_name))

    def remove_product_from_cart(self, product_name: str):
        self.page.click(self._remove_button(product_name))

    def get_cart_badge_count(self) -> str:
        if self.page.locator(self.CART_BADGE).count() == 0:
            return "0"
        return self.page.locator(self.CART_BADGE).inner_text()

    def go_to_cart(self):
        self.page.click(self.CART_ICON)

    def sort_products(self, option_value: str):
        self.page.select_option(self.SORT_DROPDOWN, option_value)

    def get_product_names(self):
        return self.page.locator(self.ITEM_NAME).all_inner_texts()

    def logout(self):
        self.page.click(self.MENU_BUTTON)
        self.page.click(self.LOGOUT_LINK)
