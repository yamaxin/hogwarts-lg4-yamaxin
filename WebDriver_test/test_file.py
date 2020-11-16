import time
from selenium import webdriver
from WebDriver_test.base import Base

class TestFile(Base):
    def test_file_upload(self):
        self.driver.get('https://www.baidu.com/')
        # 点击图片按钮
        self.driver.find_element_by_xpath('//*[@class="soutu-btn"]').click()
        time.sleep(3)
        # 点击上传文件
        upload_file = self.driver.find_element_by_xpath('//*[@class="upload-pic"]')
        upload_file.send_keys('/Users/yamaxin/python_project/hogwarts-lg4-yamaxin/img/photo.jpg')
        time.sleep(3)