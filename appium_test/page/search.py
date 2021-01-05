from appium_test.page.base_page import BasePage


class Search(BasePage):
    def search(self, value):
        # 定义value命中规则
        self._params['value'] = value
        self.steps('../page/search.yaml')

