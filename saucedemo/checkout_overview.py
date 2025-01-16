from saucedemo.base_page import BasePage


class CheckoutOverview(BasePage):
    BUTTON_FINISH_SELECTOR = '#finish'
    BUTTON_CONTINUE_SELECTOR = 'data-test="continue"'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-step-two.html'

    def click_on_finish(self):
        self.wait_for_selector_and_click(self.BUTTON_FINISH_SELECTOR)
