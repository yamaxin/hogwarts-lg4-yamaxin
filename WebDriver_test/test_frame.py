from selenium.webdriver import ActionChains

from WebDriver_test.base import Base
from selenium import webdriver
import time
class TestFrame(Base):
    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        # 进入frame
        self.driver.switch_to.frame('iframeResult')

        #拖拽
        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        time.sleep(2)

        # 点击确定弹框
        a = self.driver.switch_to.alert
        a.accept()

        # 退出frame，打印提交按钮
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id('submitBTN').text)
        time.sleep(3)

