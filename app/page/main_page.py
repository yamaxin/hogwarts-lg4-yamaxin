
#主页，进入通讯录页面
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.page.base_page import BasePage
from app.page.contact_list_page import ContactListPage


class MainPage(BasePage):
    # 首页-通讯录
    _contact_list = (MobileBy.XPATH, '//*[@text="通讯录"]')
    def goto_contactlist(self):
        '''
        进入到通讯录
        '''
        # xpath元素定位，点击通讯录
        # *代表解开元组，形成两个参数
        self.find(*self._contact_list).click()
        return ContactListPage(self.driver)
