import pytest
import yaml

# 加载yaml文件
yaml.safe_load(open('./data.yaml'))


class TestData:
    @pytest.mark.parametrize(['a','b'], yaml.safe_load(open('./data.yaml')))
    def test_param(self,a, b):
        print(a + b)

    if __name__ == '__main__':
        pytest.main()
