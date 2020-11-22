from webpageobject.demo.page.home_page import HomePage


class TestAddMember:
    def setup(self):
        self.home_page = HomePage()

    def test_add_member(self):
        name = 'yamaxin'
        account = 'yamaxin'
        phonenumber = '18678909890'

        add_member_page = self.home_page.click_add_member()
        add_member_page.add_member(name, account, phonenumber)
        result = add_member_page.get_member(name)
        assert result