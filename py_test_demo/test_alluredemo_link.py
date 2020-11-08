import allure

@allure.link('http://www.baidu.com',name='链接')
def test_with_link():
    print('这是一条加了链接的测试')
    pass

TEST_CASE_LINK = 'https://jira.mingyuanyun.com'
@allure.testcase(TEST_CASE_LINK, '登录用例')
def test_with_testcase_link():
    print('这是一条测试用例的链接，链接到测试用例里面')
    pass

# --allure-link-pattern=issue:https://jira.mingyuanyun.com/{}
@allure.issue('GZL-1511','这是一个bug')
def test_with_issue_link():
    pass