from selenium import webdriver
import time
from selenium.webdriver import TouchActions
import pytest


class TestHTouchActions():
    def setup(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(chrome_options=opt)
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_touch(self):
        el = self.driver.find_element_by_id('kw')
        el_search = self.driver.find_element_by_id('su')
        el.send_keys('selenium测试')

        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()

        action.scroll_from_element(el_search,0,10000).perform()
        time.sleep(3)


    def teardown(self):
        self.driver.quit()
        
if __name__=='__main__':
    pytest.main()