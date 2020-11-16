from selenium import webdriver
import pytest

class TestAssert():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ceshiren.com/')
        self.driver.maximize_window()
        # 隐式等待，每一次调用find_element方法时激活该方法，每隔0.5s寻找一次元素
        self.driver.implicitly_wait(5)

    def test_assert(self):
        element = self.driver.find_element_by_link_text('所有分类')
        element.click()
        # # 点击后，class变为active,重新获取元素
        element1 = self.driver.find_element_by_link_text('所有分类')
        result = element1.get_attribute('class')
        # 断言
        assert 'active' == result


    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main()