from appium import webdriver
import pytest
from hamcrest import  *

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


    def test_attr(self):
        # 点击搜索框
        search_element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # 获取属性
        print(search_element.get_attribute('content-desc'))
        print(search_element.get_attribute('resource-id'))
        print(search_element.get_attribute('enabled'))
        print(search_element.get_attribute('clickable'))
        print(search_element.get_attribute('bounds'))
        # 判断搜索框是否可用
        search_enabled = search_element.is_enabled()
        # 查看name属性值
        print(search_element.text)
        # 打印搜索框坐标
        print(search_element.location)
        # 打印搜索框宽高
        print(search_element.size)

        assert 'search' in search_element.get_attribute('resource-id')

    def test_hamcrest(self):
        assert_that(10, equal_to(10), '这是一个提示信息')
        assert_that(10, close_to(11,2), '接近上下浮动的值')
        # 前面字符串包含后面的字符串
        assert_that('contains some string', contains_string("string"))




    def teardown(self):
        # 返回上一个页面，实际操作中需要点击几次back，就添加几个back用例
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

if __name__=="__main__":
    pytest.main()