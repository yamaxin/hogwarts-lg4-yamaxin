

# 通讯录页面
# from app.page.member_invite_menu_page import MemberInviteMenuPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.page.base_page import BasePage


class ContactListPage(BasePage):
    def add_member(self):
        # 循环导入时，使用局部导入
        from app.page.member_invite_menu_page import MemberInviteMenuPage

        # 滚动查找，点击添加成员
        self.find_by_scroll('添加成员').click()

        return MemberInviteMenuPage(self.driver)