import pytest
import yaml

from src.caculator import caculator

def get_case_data():
    with open("./data.yml",encoding='utf-8') as f:
        data=yaml.safe_load(f)
        return [data["add"],data["minus"],data["multipy"],data["devide"]]


class TestCaculator():
    def setup_class(self):
        print("class开始")
        self.cal = caculator()
    def teardown_class(self):
        print("class结束")

    def setup_method(self):
        print("开始计算")
    def teardown_method(self):
        print("计算结束")
    @pytest.mark.parametrize('a,b,exc_data',get_case_data()[0])
    def test_add(self,a,b,exc_data):
        print("加法")
        assert self.cal.add(a,b)==exc_data

    @pytest.mark.parametrize('a,b,exc_data',get_case_data()[1])
    def test_minus(self,a,b,exc_data):
        print("减法")
        assert self.cal.minus(a, b) == exc_data

    @pytest.mark.parametrize('a,b,exc_data',get_case_data()[2])
    def test_multipy(self,a,b,exc_data):
        print("乘法")
        assert self.cal.multipy(a, b) == exc_data


    @pytest.mark.parametrize('a,b,exc_data',get_case_data()[3])
    def test_devide(self,a,b,exc_data):
        print("除法")
        assert self.cal.devide(a, b) == exc_data
