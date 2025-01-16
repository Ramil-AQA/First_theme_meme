from saucedemo.base_page import BasePage


class Checkout_complete_page(BasePage):
    BURGER_MENU_BUTTON_SELECT = '#react-burger-menu-btn'
    LOGOUT_BUTTON_SELECTOR = '#logout_sidebar_link'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-complete.html'

    def click_logout(self):
        self.wait_for_selector_and_click(self.BURGER_MENU_BUTTON_SELECT)
        self.wait_for_selector_and_click(self.LOGOUT_BUTTON_SELECTOR)