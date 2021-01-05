from appium import webdriver

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import *


class TestDW:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = True
        # desired_caps['dontStopAppOnReset'] = True
        desired_caps['skipDeviceIntialization'] = True
        # 切换输入法为中文输入法
        desired_caps['unicodeKeyBoard'] = True
        desired_caps['resetKeyBoard'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    @pytest.mark.skip
    def test_search(self):
        # 启动雪球，搜索中文阿里巴巴
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")

        # 在搜索结果里选择阿里巴巴，然后点击
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        # 获取阿里巴巴股价，并判断这只股价的价格>200
        current_price = float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
        expected_price = 170
        # 断言
        # assert current_price > 200
        assert_that(current_price,close_to(expected_price,expected_price*0.1))

    @pytest.mark.skip
    def test_attr(self):
        # 点击搜索框
        search_element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # 判断搜索框是否可用
        search_enabled = search_element.is_enabled()
        # 查看name属性值
        print(search_element.text)
        # 打印搜索框坐标
        print(search_element.location)
        # 打印搜索框宽高
        print(search_element.size)

        # 点击搜索框
        if search_enabled==True:
            search_element.click()

            # 输入alibaba
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('alibaba')

            # 判断阿里巴巴是否可见，如果可见，打印搜索成功，否则发音搜索失败
            alibaba_element = self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
            # alibaba_text.is_displayed()
            alibaba_displayed = alibaba_element.get_attribute('displayed')
            if alibaba_displayed =='true':
                print('搜索成功')
            else:
                print('搜索失败')


    def test_touchaction1(self):
        action = TouchAction(self.driver)
        # 获取像素宽高
        window_rect = self.driver.get_window_rect()
        width = window_rect['witdh']
        height = window_rect['height']

        # 定义滑动起点和终点
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)

        # 滑动页面
        action.press(x=1, y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()




    def teardown(self):
        # 返回上一个页面，实际操作中需要点击几次back，就添加几个back用例
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

if __name__=="__main__":
    pytest.main()


