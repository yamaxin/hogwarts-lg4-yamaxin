import shelve
import time
from time import sleep
import pytest

from selenium import webdriver
# 复用浏览器，免登录，借助浏览器remote-debug模式
# Mac command中启动谷歌浏览器debug（使用tab键联想）：/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
from selenium.webdriver.chrome.options import Options


class TestWX:
    def setup(self):
        # 定义option
        option = Options()
        # 指定optipn的debug地址，注意端口要与命令行启动的端口保持一致
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.implicitly_wait(5)

    @pytest.mark.skip
    def test_case1(self):
        # self.driver.find_element_by_id('menu_contacts').click()
        # sleep(3)
        pass

    @pytest.mark.skip
    def test_cookie(self):
        cookies = self.driver.get_cookies()
        print(cookies)
        for cookie in cookies:
            # invalid expiry解决方法
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            # 添加cookie
            self.driver.add_cookie(cookie)


    def test_cookies(self):
        # shelve模块，python自带的对象持久化存储，可以存储cookies
        # option+command+l格式化显示cookies
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '3782497195354870'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1605829484, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '59gqfgh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1637333948, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1608389948, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'}]
        db = shelve.open('cookies')
        db['cookie'] = cookies
        db.close()
        # 运行后生成cookies.db文件，二进制方式存储cookies，然后注释掉cookies

        # 打开无痕页面
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # 加入cookie
        for cookie in cookies:
            # invalid expiry解决方法
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            # 添加cookie
            self.driver.add_cookie(cookie)

        # 刷新当前页面，获取登录状态
        self.driver.refresh()
        time.sleep(3)
        # 导入通讯录
        self.driver.find_element_by_css_selector('.ww_indexImg ww_indexImg_Import:nth-child(2)').click()
        time.sleep(3)
        # 上传文件
        file = self.driver.find_element_by_css_selector('.ww_fileImporter_fileContainer_uploadInputMask')
        file.send_keys('/Users/yamaxin/python_project/hogwarts-lg4-yamaxin/WebDriver_test/客户数据规模测算表-流程中心（千亿）_终稿(2-06).xlsx')
        result = file.text
        assert '客户数据规模测算表-流程中心（千亿）_终稿(2-06).xlsx' == result

    def teardown(self):
        self.driver.quit()

