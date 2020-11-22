from selenium.webdriver.common.by import By
from webpageobject.demo.page.base_page import BasePage



class AddMemberPage(BasePage):
    def add_member(self, name, account, phonenumber):
        # 输入姓名
        self.find(By.ID, 'username').send_keys(name)
        # 输入账号
        self.find(By.ID, 'memberAdd_acctid').send_keys(account)
        # 输入手机电话
        self.find(By.ID, 'memberAdd_phone').send_keys(phonenumber)

        # 点击保存
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def get_member(self, value):
        # 显示等待，知道元素可点击，才执行
        locator = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(locator)
        titles_total = []
        while True:
            # 定位列表所有member
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            # 获取列表所有member的名字
            titles = [element.get_attribute('title') for element in elements]
            if value in titles:
                return True
            titles_total.extend(titles)

            # 获取页数/总页数，:str属于类型提示
            page:str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
            # 通过split分割页数/总页数
            num, total = page.split('/', 1)

            if int(num) == int(total):
                return False
            else:
                # 获取翻页按钮，点击
                self.find(By.CSS_SELECTOR, '.ww_commonImg_PageNavArrowRightNormal').click()


        return titles_total




