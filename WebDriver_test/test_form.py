from selenium import webdriver
import time
import pytest

class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com/account/sign_in')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_form(self):
        username = self.driver.find_element_by_id('user_login')
        password = self.driver.find_element_by_id('user_password')
        username.send_keys('635284721@qq.com')
        password.send_keys('15872411180k')
        self.driver.find_element_by_id('user_remember_me').click()
        self.driver.find_element_by_name('commit').click()
        time.sleep(5)



    def teardown(self):
        self.driver.quit()

if __name__=='__main__':
    pytest.main()