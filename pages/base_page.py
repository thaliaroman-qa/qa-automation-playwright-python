"""Base Page Object with common helpers shared across all pages."""
from playwright.sync_api import Page


class BasePage:
    URL = ""

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)
        return self

    def title(self) -> str:
        return self.page.title()

    def current_url(self) -> str:
        return self.page.url
