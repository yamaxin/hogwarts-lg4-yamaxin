import pytest
class TestData:
    @pytest.mark.parametrize('a,b', [
        (10, 20),
        (10, 30),
        (3, 9)
    ])
    def test_param(self,a, b):
        print(a + b)

    if __name__ == '__main__':
        pytest.main()

