"""Page Object for the SauceDemo login page."""
from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page: Page):
        super().__init__(page)

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR_MESSAGE).inner_text()

    def is_error_displayed(self) -> bool:
        return self.page.locator(self.ERROR_MESSAGE).is_visible()

    def is_login_button_visible(self) -> bool:
        return self.page.locator(self.LOGIN_BUTTON).is_visible()
