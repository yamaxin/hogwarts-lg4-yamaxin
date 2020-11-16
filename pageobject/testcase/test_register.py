from pageobject.page.main import Main


class TestRegister:
    def setup(self):
        # 声明main函数对象，将对象实例化
        self.main = Main()

    def test_register(self):
        # main调用自己的方法goto_register(),goto_register()继续调用register()
        assert self.main.goto_register().register()

    def test_register2(self):
        # main调用自己的方法goto_login(),goto_login()继续调用goto_register()，继续调用register()
        assert self.main.goto_login().goto_register().register()





