import allure
import pytest
from utils.helpers import random_email   # if you put the random_email helper in utils/helpers.py
from utils.helpers import random_email
# Import Page Objects
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage



import allure
import pytest

@pytest.mark.e2e
@allure.feature("Demo Web Shop E2E Flow")
@allure.story("User Registration, Login, Shopping, Checkout, Order Confirmation")
@allure.severity(allure.severity_level.BLOCKER)
def test_demowebshop_full_checkout(page):
    home = HomePage(page)
    register = RegisterPage(page)
    login = LoginPage(page)
    product = ProductPage(page)
    cart = CartPage(page)

    firstname, lastname = "John", "Doe"
    email, password = random_email(), "Password123!"

    try:
        with allure.step("Navigate to homepage"):
            home.navigate()

        with allure.step("Register a new user"):
            home.click_register()
            register.register(firstname, lastname, email, password)

        with allure.step("Logout and login again"):
            home.click_logout()
            home.click_login()
            login.login(email, password)

        with allure.step("Search for product and add to cart"):
            home.search_product("computer")
            product.wait_for_results()
            product.add_configured_computer_to_cart()

        with allure.step("Proceed to checkout"):
            cart.open_cart()
            cart.verify_item_in_cart()  # now navigates properly to checkout page



    except Exception as e:

        screenshot_path = "AllureReports/screenshots/failure_step.png"

        page.screenshot(path=screenshot_path)

        allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG)

        raise e

