from selenium import webdriver
from WebDriver_test.base import Base
import time
import pytest

class TestJS(Base):
    def test_js(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        # 定位搜索元素
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        time.sleep(3)
        # 滑动至底部
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        # 点击下一页
        self.driver.find_element_by_xpath('//*[@id="page"]//a[1]//span[2]').click()
        time.sleep(3)
        # 获取页面性能数据
        for code in ['return document.title', 'return JSON.stringify(performance.timing)']:
            print(self.driver.execute_script(code))

        # 返回第一个return的值
        print(self.driver.execute_script("return document.title; return JSON.stringify(performance.timing)"))

    @pytest.mark.skip
    def test_datetime(self):
        self.driver.get('https://www.12306.cn/index/')
        # 定位时间元素,清除只读属性
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        # 传入日期
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        time.sleep(3)