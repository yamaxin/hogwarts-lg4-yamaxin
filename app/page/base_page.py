# 存放driver初始化、find、get_toast
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # 打印日志，python自带的方法
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='../log/myapp.log',
                        filemode='w')
    
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self,by,locator):
        logging.info('find:')
        logging.info(by)
        logging.info(locator)
        return self.driver.find_element(by,locator)

    def find_by_scroll(self, text):
        logging.info('find_by_scroll')
        logging.info(text)
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 f'.text("{text}").instance(0));')

    def get_toast_text(self):
        logging.info('get_toast_text：')
        result = self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        logging.info(result)
        return result


