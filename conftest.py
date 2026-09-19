# conftest.py
import pytest
from playwright.sync_api import Page

@pytest.fixture
def logged_in_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    return page