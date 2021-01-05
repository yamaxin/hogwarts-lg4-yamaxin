# 手动添加,编辑成员页面
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.page.base_page import BasePage
from app.page.member_invite_menu_page import MemberInviteMenuPage


class ContactAddPage(BasePage):
    def edit_contact(self,name,gender,phonenum):
        '''
        编辑成员信息
        '''

        # 输入姓名
        self.find(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys(name)

        # 点击选择性别
        self.find(MobileBy.XPATH, '//*[@text="性别"]/..//*[@text="男"]').click()
        # 选择男，女
        if gender == "男":
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()

        # 填写手机号
        self.find(MobileBy.XPATH, '//*[@text="手机号"]').send_keys(phonenum)

        # 保存
        self.find(MobileBy.XPATH, '//*[@text="保存"]').click()

        return MemberInviteMenuPage(self.driver)
