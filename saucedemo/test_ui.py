from faker import Faker

from saucedemo.checkout_complete_page import Checkout_complete_page
from saucedemo.checkout_overview import CheckoutOverview
from saucedemo.checkout_page import CheckoutPage

from saucedemo.inventory_page import InventoryPage
from saucedemo.login_auth_page import LoginPage


def test_checkout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    checkout_overview = CheckoutOverview(page)
    logout = Checkout_complete_page(page)
    login_page.registration('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form('asd', 'asddsa', '123123123')
    checkout_page.click_on_continue()
    checkout_overview.click_on_finish()
    logout.click_logout()

