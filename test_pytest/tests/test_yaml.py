import data as data

from test_pytest.core.calc import Calc
import pytest
import yaml


def load_data(path='data.yaml'):
    with open(path) as f:
        data = yaml.safe_load(f)
        keys = ','.join(data[0].keys())
        values = [list(d.values()) for d in data]
        data = {'keys': keys, 'values': values}
        return data

class TestCalc:
    # 赋值变量
    data = load_data()

    @classmethod
    def setup_class(cls):
        print('setup_class method')
        cls.calc = Calc()

    # @classmethod
    # def load_data(cls, path='data.yaml'):
    #     with open(path) as f:
    #         data = yaml.safe_load(f)
    #         return data

    @pytest.mark.parametrize(
        data['keys'],
        data['values'])
    def test_div_data(self,a,b,c):
        # 测试除法正确性
        assert self.calc.div(a,b) == c