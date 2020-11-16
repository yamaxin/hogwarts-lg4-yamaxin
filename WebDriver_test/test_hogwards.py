from selenium import webdriver
import time

class  TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_hogwards(self):
        self.driver.find_element_by_link_text('社团').click()
        self.driver.find_element_by_link_text('求职面试圈').click()
        self.driver.find_element_by_xpath("//a[@href='/topics/25244']").click()
        time.sleep(3)

    def teardown(self):
        self.driver.quit()
