from appium_test.page.base_page import BasePage
from appium_test.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps('../page/main.yaml')
        return Market(self._driver)
