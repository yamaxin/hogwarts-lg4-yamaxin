import allure
import pytest
from selenium import webdriver
import time

@allure.testcase('http://jira.mingyuanyun.com')
@allure.feature('百度搜索')
@pytest.mark.parametrize('test_data',['allure','pytest','unittest'])
def test_steps_demo(test_data):
    with allure.step('打开百度网页'):
        driver = webdriver.Chrome()
        driver.get('http://www.baidu.com')
        driver.maximize_window()

    with allure.step('输入搜索词'):
        driver.find_element_by_id('kw').send_keys(test_data)
        time.sleep(2)
        driver.find_element_by_id('su').click()
        time.sleep(2)

    with allure.step('保存图片'):
        driver.save_screenshot('./result/b.png')
        allure.attach.file('./result/b.png', attachment_type=allure.attachment_type.PNG)
        allure.attach('<head></head><body>首页</body>', 'Attach with HTML type', allure.attachment_type.HTML)
    driver.quit()