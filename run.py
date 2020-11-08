from util.HTMLTestRunner_PY3 import HTMLTestRunner
import unittest

if __name__ == '__main__':
    report_title = 'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = './Report.html'

    test_dir = './testcases'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)
