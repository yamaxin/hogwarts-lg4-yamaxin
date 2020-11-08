import allure
import pytest

def test_attach_text():
    allure.attach('这是一个纯文本',attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一段htmlbody模块</body>", "html模块", attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file('/Users/yamaxin/python_project/hogwarts-lg4-yamaxin/py_test_demo/resource/photo.jpg',name='ing',attachment_type=allure.attachment_type.JPG)