from appium import webdriver

# capabilities设置
# 不要对应用进行reset，默认使用之前的登录信息，配置noReset
desire_cap = {
  "platformName": "android",
  "deviceName": "emulator-5554",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "noReset": True
}
# 初始化driver
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_cap)
# 隐式等待
driver.implicitly_wait(10)
el1 = driver.find_element_by_id("com.xueqiu.android:id/home_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.click()
el3.send_keys("alibba")
el4 = driver.find_element_by_id("com.xueqiu.android:id/name")
el4.click()
el5 = driver.find_element_by_id("com.xueqiu.android:id/topic_text")
el5.click()
