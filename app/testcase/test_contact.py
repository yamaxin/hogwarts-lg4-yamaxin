from app.page.app import App


class TestWX:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()


    def test_add_contact(self):
        name = "Wu3"
        gender = '男'
        phonenum = '18672909814'

        result = self.main.goto_contactlist().add_member().add_member_manul().edit_contact(name,gender,phonenum).verify_toast()
        assert result == '添加成功'

    def teardown(self):
        self.app.stop()

