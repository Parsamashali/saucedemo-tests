import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("username, password, expected_result", [
    ("standard_user", "secret_sauce", "success"),
    ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
    ("standard_user", "wrong_password", "Username and password do not match any user in this service"),
    ("", "", "Username is required"),
])
def test_login(page: Page, username, password, expected_result):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

    if expected_result == "success":
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    else:
        expect(page.locator('[data-test="error"]')).to_contain_text(expected_result)