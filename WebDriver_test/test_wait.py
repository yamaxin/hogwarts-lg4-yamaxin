from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ceshiren.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_wait(self):
        self.driver.find_element_by_link_text('热门').click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="PyTest测试框架"]')))
        self.driver.find_element_by_xpath('//a[text()="PyTest测试框架"]').click()


    def teardown(self):
        self.driver.quit()