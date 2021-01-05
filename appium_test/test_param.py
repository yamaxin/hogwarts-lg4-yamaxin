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

    @pytest.mark.parametrize('search_key,type,expect_price',
                             [('alibaba','BABA',250),
                              ('xiaomi','01810',25)
                              ])
    def test_search(self,search_key, type, expect_price):
        '''打开雪球
        1、点击搜索
        2、搜索alibab
        3、点击第一个搜索结果
        4、判断股票价格
        '''
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys(search_key)
        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/name"]').click()
        # 获取阿里巴巴股价
        current_price = float(self.driver.find_element(MobileBy.XPATH,f'//*[@text="{type}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text)
        assert_that(current_price, close_to(expect_price,expect_price*0.1))
        print(f'当前的价格是{current_price}')


    def teardown(self):
        # 返回上一个页面，实际操作中需要点击几次back，就添加几个back用例
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

if __name__=="__main__":
    pytest.main()