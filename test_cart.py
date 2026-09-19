import pytest
from playwright.sync_api import Page, expect


def test_add_one_product_to_cart(logged_in_page):
    logged_in_page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    expect(logged_in_page.locator(".shopping_cart_badge")).to_have_text("1")


def test_add_multiple_products_to_cart(logged_in_page):
    logged_in_page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    logged_in_page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    logged_in_page.locator('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    expect(logged_in_page.locator(".shopping_cart_badge")).to_have_text("3")


def test_remove_one_product_from_cart(logged_in_page):
    logged_in_page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    logged_in_page.locator('[data-test="remove-sauce-labs-backpack"]').click()
    expect(logged_in_page.locator(".shopping_cart_badge")).to_be_hidden()


def test_remove_multiple_products_from_cart(logged_in_page):
    logged_in_page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    logged_in_page.locator('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    logged_in_page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    logged_in_page.locator('[data-test="remove-sauce-labs-backpack"]').click()
    logged_in_page.locator('[data-test="remove-sauce-labs-bolt-t-shirt"]').click()
    logged_in_page.locator('[data-test="remove-sauce-labs-bike-light"]').click()
    expect(logged_in_page.locator(".shopping_cart_badge")).to_be_hidden()