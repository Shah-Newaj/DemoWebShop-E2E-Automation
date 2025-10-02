import sys, os
# Add project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import random, string
import pytest
import allure
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def random_email():
    return "testuser_" + ''.join(random.choices(string.ascii_lowercase, k=6)) + "@example.com"

@allure.feature("Magento E2E Flow")
@allure.story("User Registration, Login, Shopping, Checkout")
@allure.severity(allure.severity_level.CRITICAL)
def test_magento_full_flow(page):
    home = HomePage(page)
    register = RegisterPage(page)
    login = LoginPage(page)
    product = ProductPage(page)
    cart = CartPage(page)

    firstname, lastname = "John", "Doe"
    email, password = random_email(), "Password123!"

    with allure.step("Navigate to Homepage"):
        home.navigate()

    with allure.step("Register a new user"):
        home.click_create_account()
        register.register(firstname, lastname, email, password)

    with allure.step("Logout and Login again"):
        home.click_sign_out()
        home.click_sign_in()
        login.login(email, password)

    with allure.step("Search for a product and add to cart"):
        home.search_product("jacket")
        product.wait_for_results()
        product.add_first_product_to_cart()

    with allure.step("Proceed to checkout"):
        cart.proceed_to_checkout()
