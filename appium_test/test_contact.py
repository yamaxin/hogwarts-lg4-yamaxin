from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWX:
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": True
        }
        # 初始化driver
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_cap)
        # 隐式等待
        self.driver.implicitly_wait(10)

    def test_contact(self):
        name = "Wu"
        gender = '男'
        phonenum = '18672909812'
        # xpath元素定位，点击通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()

        # 滚动查找，点击添加成员
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        # 点击手动输入添加
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()

        # 输入姓名
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys(name)
        # self.driver.find_element(MobileBy.XPATH, '// *[contains( @ text, "姓名")] /../ *[@text="必填"]')

        # 点击选择性别
        self.driver.find_element(MobileBy.XPATH, '//*[@text="性别"]/..//*[@text="男"]').click()
        # 选择男，女
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        # 填写手机号
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手机号"]').send_keys(phonenum)

        # 保存
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        # time.sleep(3)
        # 打印页面布局结构
        # print(self.driver.page_source)

        # 校验是否保存成功
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="添加保存"]')
        result = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        assert result == '添加成功'

    def teardown(self):
        self.driver.quit()