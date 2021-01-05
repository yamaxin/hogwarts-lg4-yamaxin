# 存放app相关的操作,启动/重启app，进入主页
# 存放web相关操作
from appium import webdriver
from app.page.base_page import BasePage
from app.page.main_page import MainPage


class App(BasePage):
    def start(self):
        # 复用driver，判断driver是否为None，如果为None，则创建一个driver，如果不为None，则复用已有的driver
        if self.driver == None:
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
        else:
            # 启动app，启动的页面是desire_cap里面设置的appActivity
            self.driver.launch_app()
            # start_activity与launch_app效果一致，但需要传参数：包名和活动名
            # self.driver.start_activity("com.tencent.wework",".launch.WwMainActivity")
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()


    def goto_main(self):
        # 进入首页
        return MainPage(self.driver)