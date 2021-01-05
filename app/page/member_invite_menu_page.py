
# 添加成员列表页面
# from app.page.contact_add_page import ContactAddPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.page.base_page import BasePage


class MemberInviteMenuPage(BasePage):
    def add_member_manul(self):
        from app.page.contact_add_page import ContactAddPage
        # 点击手动输入添加
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return ContactAddPage(self.driver)

    def verify_toast(self):
        result = self.get_toast_text()
        return result
