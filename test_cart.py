import pytest
from playwright.sync_api import Page, expect

def test_remove_multiple_products_from_cart(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    page.locator('[data-test="remove-sauce-labs-backpack"]').click()
    page.locator('[data-test="remove-sauce-labs-bolt-t-shirt"]').click()
    page.locator('[data-test="remove-sauce-labs-bike-light"]').click()

    expect(page.locator(".shopping_cart_badge")).to_be_hidden()