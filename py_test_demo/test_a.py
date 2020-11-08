import pytest

def inc(x):
    return x + 1

@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,20),
    ('a','a1'),
    (3,4),
    (5,6)
                         ])
# pytest参数化方法
def test_answer(a,b):
    assert inc(a) == b

def test_answer1():
    assert inc(4) == 5

@pytest.fixture()
# pytest装饰器
def login():
    username = 'Jerry'
    return '登录操作'+ username

class TestDemo:
    def test_a(self,login):
        print(f'a  username={login}')

    def test_b(self):
        print('b')

    def test_c(self,login):
        print('c')
        print(f'c  username={login}')

if __name__=='__main__':
    pytest.main(['test_a.py::TestDemo','-v'])