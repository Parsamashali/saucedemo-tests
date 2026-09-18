import pytest
from playwright.sync_api import Page, expect

def test_successful_checkout(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    page.locator(".shopping_cart_link").click()
    page.locator("#checkout").click()

    page.locator("#first-name").fill("parsa")
    page.locator("#last-name").fill("mashali")
    page.locator("#postal-code").fill("12345")
    page.locator("#continue").click()
    page.locator("#finish").click()

    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")

    import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("first_name, last_name, zip_code, expected_error", [
    ("", "mashali", "12345", "Error: First Name is required"),
    ("parsa", "", "12345", "Error: Last Name is required"),
    ("parsa", "mashali", "", "Error: Postal Code is required"),
])
def test_checkout_missing_fields(page: Page, first_name, last_name, zip_code, expected_error):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    page.locator(".shopping_cart_link").click()
    page.locator("#checkout").click()

    page.locator("#first-name").fill(first_name)
    page.locator("#last-name").fill(last_name)
    page.locator("#postal-code").fill(zip_code)
    page.locator("#continue").click()

    expect(page.locator(".error-message-container")).to_have_text(expected_error)