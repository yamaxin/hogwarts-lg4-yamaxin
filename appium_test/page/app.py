from appium_test.page.base_page import BasePage
from appium import webdriver
from appium_test.page.main import Main


class App(BasePage):
    def start(self):
        _package = 'com.xueqiu.android'
        _activity = 'com.xueqiu.android.common.MainActivity'
        if self._driver is None:
            caps = {}
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '6.0'
            caps['deviceName'] = 'emulator-5554'
            caps['appPackage'] = _package
            caps['appActivity'] = _activity
            caps['noReset'] = True
            caps['dontStopAppOnReset'] = True
            caps['skipDeviceIntialization'] = True
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self._driver.implicitly_wait(10)
        else:
            self._driver.start_activity(_package,_activity)

        return self

    def main(self):
        return Main(self._driver)

