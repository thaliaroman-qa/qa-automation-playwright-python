"""Page Object for the SauceDemo shopping cart page."""
from playwright.sync_api import Page
from pages.base_page import BasePage


class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    PAGE_TITLE = ".title"
    CART_ITEM = ".cart_item"
    ITEM_NAME = ".inventory_item_name"
    CONTINUE_SHOPPING_BUTTON = "#continue-shopping"
    CHECKOUT_BUTTON = "#checkout"

    def __init__(self, page: Page):
        super().__init__(page)

    def _remove_button(self, product_name: str):
        slug = product_name.lower().replace(" ", "-").replace("(", "").replace(")", "")
        return f"[data-test='remove-{slug}']"

    def is_loaded(self) -> bool:
        return self.page.locator(self.PAGE_TITLE).inner_text() == "Your Cart"

    def get_cart_items(self):
        return self.page.locator(self.ITEM_NAME).all_inner_texts()

    def get_cart_items_count(self) -> int:
        return self.page.locator(self.CART_ITEM).count()

    def remove_product(self, product_name: str):
        self.page.click(self._remove_button(product_name))

    def continue_shopping(self):
        self.page.click(self.CONTINUE_SHOPPING_BUTTON)

    def checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)
