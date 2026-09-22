"""Page Object for the SauceDemo checkout flow (steps one, two and completion)."""
from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    URL = "https://www.saucedemo.com/checkout-step-one.html"

    # Step one - information form
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    ERROR_MESSAGE = "[data-test='error']"

    # Step two - overview
    FINISH_BUTTON = "#finish"
    CANCEL_BUTTON = "#cancel"
    SUMMARY_TOTAL_LABEL = ".summary_total_label"

    # Complete
    COMPLETE_HEADER = ".complete-header"
    BACK_HOME_BUTTON = "#back-to-products"

    def __init__(self, page: Page):
        super().__init__(page)

    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.FIRST_NAME_INPUT, first_name)
        self.page.fill(self.LAST_NAME_INPUT, last_name)
        self.page.fill(self.POSTAL_CODE_INPUT, postal_code)
        self.page.click(self.CONTINUE_BUTTON)

    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR_MESSAGE).inner_text()

    def finish_checkout(self):
        self.page.click(self.FINISH_BUTTON)

    def get_total_summary(self) -> str:
        return self.page.locator(self.SUMMARY_TOTAL_LABEL).inner_text()

    def get_complete_header(self) -> str:
        return self.page.locator(self.COMPLETE_HEADER).inner_text()

    def is_order_complete(self) -> bool:
        return self.page.locator(self.COMPLETE_HEADER).is_visible()
