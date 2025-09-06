import pytest

import time

from setup.driver_setup import DriverSetup
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage

@pytest.fixture(scope="session")
def driver():
    #setup
    driver_setup = DriverSetup()
    driver = driver_setup.start_driver()
    time.sleep(5)

    #teardown
    yield driver
    try:
        account = AccountPage(driver)
        account.click_account_tab()
        time.sleep(2)
        account.click_sign_out_button()  # Replace with actual logout method
        time.sleep(2)
        print("Logged out successfully.")
    except Exception as e:
        print(f"Logout failed or skipped: {e}")

    driver_setup.stop_driver()

def test_successful_login(driver):
    """Test to login to mumzworld app"""
    account = AccountPage(driver)
    account.click_account_tab()
    time.sleep(5)
    account.click_sign_in_button()
    time.sleep(2)

    login = LoginPage(driver)
    login.enter_email("hea6163@gmail.com")
    login.enter_password("Srib@2025")
    login.click_login()
    time.sleep(5)

    assert login.is_logged_in(), "Login failed"


def test_add_to_cart(driver):
    """Test to add a product to the cart"""
    search = SearchPage(driver)
    search.explore()
    time.sleep(2)
    search.search_item("Diaper")
    time.sleep(3)

    product = ProductPage(driver)
    product.select_first_product()
    time.sleep(2)
    product.add_to_cart()
    time.sleep(5)
    assert product.go_to_cart(), "item not added to the cart"
    product.close_cart()
