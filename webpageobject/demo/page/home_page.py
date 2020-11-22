from selenium.webdriver.common.by import By
from webpageobject.demo.page.add_member_page import AddMemberPage
from webpageobject.demo.page.base_page import BasePage


class HomePage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def click_add_member(self):
        # 滑动至页面底部
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        # 点击添加成员
        add_member_element = self.find(By.XPATH, '//span[text()="添加成员"]')
        add_member_element.click()
        return AddMemberPage(self.driver)
