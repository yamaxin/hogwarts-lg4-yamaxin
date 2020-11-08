from test_pytest.core.calc import Calc
import pytest
import allure


class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    def setUp(self):
        pass

    @allure.step
    def simple_step(self,step_param1, step_param2=None):
        pass

    @pytest.mark.parametrize('a,b,c', [
        (1, 2, 2),
        (-1, -1, 1),
        (-1, 1, -1),
        (-1, 0, 0),
        (999999999,999999999,999999998000000001),
        (0.2,0.3, 0.06),
        (0.4, 2, 0.8),
    ])
    def test_mul(self,a,b,c):
        self.simple_step(f'{a},{b},{c}')
        # 测试乘法正确性
        assert self.calc.mul(a,b) == c

    @pytest.mark.parametrize('a,b,c', [
        (2.03, 100, 203)
    ])
    def test_mul(self, a, b, c):
        # 测试浮点数相乘
        assert round(self.calc.mul(a, b)) == c


    @pytest.mark.parametrize('a,b', [
        ('a', 'b'),
        ('a', 0)
    ])
    def test_mul_float(self,a,b):
        # 测试乘数为字符串的场景
        with pytest.raises(TypeError):
            assert self.calc.div(a, b)


    @pytest.mark.parametrize('a,b,c', [
        (1, 2, 0.5),
        (-1, -1, 1),
        (-1, 1, -1),
        (0, 1, 0),
        (1.0,3,0.3333333333333333),
        (0.2, 0.6, 0.33333333333333337),
    ])
    def test_div(self,a,b,c):
        # 测试除法正确性
        assert self.calc.div(a,b) == c

    @pytest.mark.parametrize('a,b', [
        ('a', 0),
        ('a', 'b'),
        ('1.1', 'b')
    ])
    def test_div_zero(self, a, b):
        # 测试除法传入参数为字符串的场景
        with pytest.raises(TypeError):
            assert self.calc.div(a, b)

    @pytest.mark.parametrize('a,b', [
        (1, 0),
        (-1, 0),
        (0, 0),
        (0.1,0)
    ])
    def test_div_zero(self, a, b):
        # 测试除法处以0的场景
        with pytest.raises(ZeroDivisionError):
            assert self.calc.div(a, b)

    # 流程示例
    def test_process(self):
        # 接口调用顺序测试
        r1 = self.calc.mul(1,2)
        r2 = self.calc.div(2,1)
        assert  r1 == 2
        assert  r2 == 2





