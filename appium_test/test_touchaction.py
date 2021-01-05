from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestDW:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
        desired_caps['noReset'] = True
        # desired_caps['dontStopAppOnReset'] = True
        desired_caps['skipDeviceIntialization'] = True
        # 切换输入法为中文输入法
        desired_caps['unicodeKeyBoard'] = True
        desired_caps['resetKeyBoard'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def test_unlock(self):
        # 滑动解锁
        action = TouchAction(self.driver)
        action.press(x=165,y=230).wait(200).move_to(x=464,y=230).wait(200).move_to(x=781,y=230).wait(200).move_to(x=781,y=515).wait(200).move_to(x=781,y=849).wait(200).release().perform()


    def teardown(self):
        # 返回上一个页面，实际操作中需要点击几次back，就添加几个back用例
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

if __name__ == "__main__":
    pytest.main()