# SauceDemo Automated Testing Suite

Automated end-to-end tests for [saucedemo.com](https://www.saucedemo.com/) using Python, pytest, and Playwright.

## What This Covers

- **Login** — valid login, locked-out user, invalid credentials, empty fields
- **Cart** — adding single/multiple products, removing single/multiple products
- **Checkout** — successful purchase flow, missing required fields

## Tech Stack

- Python 3.14
- pytest
- Playwright (Chromium)

## How to Run

1. Install dependencies:

   pip install pytest pytest-playwright
   playwright install

2. Run all tests:

   python -m pytest -v

3. Run with visible browser:

   python -m pytest --headed -v

## Project Structure

    ├── test_login.py       # Login scenarios
    ├── test_cart.py        # Cart management scenarios
    └── test_checkout.py    # Checkout flow scenarios